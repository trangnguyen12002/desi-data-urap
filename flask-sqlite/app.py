from   flask import Flask, request                  # manage the app
from flask import jsonify
from   sqlalchemy       import create_engine  # used to detect if table exists
from   flask_sqlalchemy import SQLAlchemy     # manage the database
import click                                  # used to load the data
import pandas            as pd                # process pandas
from flask_marshmallow import Marshmallow
import os
import json
from flask_cors import CORS



# Invoke Flask magic
app = Flask(__name__)
#basedir = os.path.abspath(os.path.dirname(__file__))

ma = Marshmallow(app)

# SQLAlchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///db.sqlite'
#app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

# DB Object = SQLAlchemy interface
db = SQLAlchemy(app)

# Define the storage
class Data(db.Model):

    NIGHT        = db.Column(db.Integer)
    EXPID        = db.Column(db.Integer, primary_key=True )
    TILEID       = db.Column(db.Float )
    TILERA       = db.Column(db.Float)
    TILEDEC      = db.Column(db.Float )
    MJD          = db.Column(db.Float )
    SURVEY       = db.Column(db.String(10 ), default=None     )
    PROGRAM      = db.Column(db.String(10 ), default=None     )
    FAPRGRM      = db.Column(db.String(10))
    FAFLAVOR     = db.Column(db.String(30 ), default=None     )
    EXPTIME      = db.Column(db.Float    ) 
    EFFTIME_SPEC = db.Column(db.Float)
    GOALTIME = db.Column(db.Float)
    GOALTYPE = db.Column(db.String(30 ))
    MINTFRAC = db.Column(db.Float)
    AIRMASS = db.Column(db.Float)
    EBV = db.Column(db.Float)
    SEEING_ETC = db.Column(db.Float)
    EFFTIME_ETC = db.Column(db.Float)
    TSNR2_ELG = db.Column(db.Float)
    TSNR2_QSO = db.Column(db.Float)
    TSNR2_LRG = db.Column(db.Float)
    TSNR2_LYA = db.Column(db.Float)
    TSNR2_BGS = db.Column(db.Float)
    TSNR2_GPBDARK = db.Column(db.Float)
    TSNR2_GPBBRIGHT = db.Column(db.Float)
    TSNR2_GPBBACKUP = db.Column(db.Float)
    LRG_EFFTIME_DARK = db.Column(db.Float)
    ELG_EFFTIME_DARK = db.Column(db.Float)
    BGS_EFFTIME_BRIGHT = db.Column(db.Float)
    LYA_EFFTIME_DARK = db.Column(db.Float)
    GPB_EFFTIME_DARK = db.Column(db.Float)
    GPB_EFFTIME_BRIGHT = db.Column(db.Float)
    GPB_EFFTIME_BACKUP = db.Column(db.Float)
    TRANSPARENCY_GFA = db.Column(db.Float)
    SEEING_GFA = db.Column(db.Float)
    FIBER_FRACFLUX_GFA = db.Column(db.Float)
    FIBER_FRACFLUX_ELG_GFA = db.Column(db.Float)
    FIBER_FRACFLUX_BGS_GFA = db.Column(db.Float)
    FIBERFAC_GFA = db.Column(db.Float)
    FIBERFAC_ELG_GFA = db.Column(db.Float)
    FIBERFAC_BGS_GFA = db.Column(db.Float)
    AIRMASS_GFA = db.Column(db.Float)
    SKY_MAG_AB_GFA = db.Column(db.Float)
    SKY_MAG_G_SPEC = db.Column(db.Float)
    SKY_MAG_R_SPEC = db.Column(db.Float)
    SKY_MAG_Z_SPEC = db.Column(db.Float)
    EFFTIME_GFA = db.Column(db.Float)
    EFFTIME_DARK_GFA = db.Column(db.Float)
    EFFTIME_BRIGHT_GFA = db.Column(db.Float)
    EFFTIME_BACKUP_GFA = db.Column(db.Float)

    # Table constructor - called by the custom command 'load_data'
    def __init__(self, NIGHT, EXPID, TILEID, TILERA, TILEDEC, MJD, SURVEY, PROGRAM, FAPRGRM, FAFLAVOR, EXPTIME,
          EFFTIME_SPEC, \
              GOALTIME, \
              GOALTYPE, \
              MINTFRAC, \
               AIRMASS, \
                   EBV, \
            SEEING_ETC, \
           EFFTIME_ETC, \
             TSNR2_ELG, \
             TSNR2_QSO, \
             TSNR2_LRG, \
             TSNR2_LYA, \
             TSNR2_BGS, \
         TSNR2_GPBDARK, \
       TSNR2_GPBBRIGHT, \
       TSNR2_GPBBACKUP, \
      LRG_EFFTIME_DARK, \
      ELG_EFFTIME_DARK, \
    BGS_EFFTIME_BRIGHT, \
      LYA_EFFTIME_DARK, \
      GPB_EFFTIME_DARK, \
    GPB_EFFTIME_BRIGHT, \
    GPB_EFFTIME_BACKUP, \
      TRANSPARENCY_GFA, \
            SEEING_GFA, \
    FIBER_FRACFLUX_GFA, \
FIBER_FRACFLUX_ELG_GFA, \
FIBER_FRACFLUX_BGS_GFA, \
          FIBERFAC_GFA, \
      FIBERFAC_ELG_GFA, \
      FIBERFAC_BGS_GFA, \
           AIRMASS_GFA, \
        SKY_MAG_AB_GFA, \
        SKY_MAG_G_SPEC, \
        SKY_MAG_R_SPEC, \
        SKY_MAG_Z_SPEC, \
           EFFTIME_GFA, \
      EFFTIME_DARK_GFA, \
    EFFTIME_BRIGHT_GFA, \
    EFFTIME_BACKUP_GFA):
        self.NIGHT = NIGHT
        self.EXPID      = EXPID
        self.TILEID     = TILEID
        self.TILERA     = TILERA
        self.TILEDEC    = TILEDEC
        self.MJD        = MJD
        self.SURVEY     = SURVEY
        self.PROGRAM    = PROGRAM
        self.FAPRGRM    = FAPRGRM
        self.FAFLAVOR   = FAFLAVOR
        self.EXPTIME    = EXPTIME 
        self.EFFTIME_SPEC = EFFTIME_SPEC
        self.GOALTIME = GOALTIME
        self.GOALTYPE = GOALTYPE
        self.MINTFRAC = MINTFRAC
        self.AIRMASS = AIRMASS
        self.EBV = EBV
        self.SEEING_ETC = SEEING_ETC
        self.EFFTIME_ETC = EFFTIME_ETC
        self.TSNR2_ELG = TSNR2_ELG
        self.TSNR2_QSO = TSNR2_QSO
        self.TSNR2_LRG = TSNR2_LRG
        self.TSNR2_LYA = TSNR2_LYA
        self.TSNR2_BGS = TSNR2_BGS
        self.TSNR2_GPBDARK = TSNR2_GPBDARK
        self.TSNR2_GPBBRIGHT = TSNR2_GPBBRIGHT
        self.TSNR2_GPBBACKUP = TSNR2_GPBBACKUP
        self.LRG_EFFTIME_DARK = LRG_EFFTIME_DARK
        self.ELG_EFFTIME_DARK = ELG_EFFTIME_DARK
        self.BGS_EFFTIME_BRIGHT = BGS_EFFTIME_BRIGHT
        self.LYA_EFFTIME_DARK = LYA_EFFTIME_DARK
        self.GPB_EFFTIME_DARK = GPB_EFFTIME_DARK
        self.GPB_EFFTIME_BRIGHT = GPB_EFFTIME_BRIGHT
        self.GPB_EFFTIME_BACKUP = GPB_EFFTIME_BACKUP
        self.TRANSPARENCY_GFA = TRANSPARENCY_GFA
        self.SEEING_GFA = SEEING_GFA
        self.FIBER_FRACFLUX_GFA = FIBER_FRACFLUX_GFA
        self.FIBER_FRACFLUX_ELG_GFA = FIBER_FRACFLUX_ELG_GFA
        self.FIBER_FRACFLUX_BGS_GFA = FIBER_FRACFLUX_BGS_GFA
        self.FIBERFAC_GFA = FIBERFAC_GFA
        self.FIBERFAC_ELG_GFA = FIBERFAC_ELG_GFA
        self.FIBERFAC_BGS_GFA = FIBERFAC_BGS_GFA
        self.AIRMASS_GFA = AIRMASS_GFA
        self.SKY_MAG_AB_GFA = SKY_MAG_AB_GFA
        self.SKY_MAG_G_SPEC = SKY_MAG_G_SPEC
        self.SKY_MAG_R_SPEC = SKY_MAG_R_SPEC
        self.SKY_MAG_Z_SPEC = SKY_MAG_Z_SPEC
        self.EFFTIME_GFA = EFFTIME_GFA
        self.EFFTIME_DARK_GFA = EFFTIME_DARK_GFA
        self.EFFTIME_BRIGHT_GFA = EFFTIME_BRIGHT_GFA
        self.EFFTIME_BACKUP_GFA = EFFTIME_BACKUP_GFA

    # The string representation of the class
    #def __repr__(self):
    #    return str(self.EXPID) + ' - ' + str(self.EXPTIME) 

class DataSchema(ma.Schema):
  class Meta:
    fields = ('NIGHT', 'EXPID', 'TILEID', 'TILERA', 'TILEDEC', 'MJD', 'SURVEY',
       'PROGRAM', 'FAPRGRM', 'FAFLAVOR', 'EXPTIME', 'EFFTIME_SPEC', 'GOALTIME',
       'GOALTYPE', 'MINTFRAC', 'AIRMASS', 'EBV', 'SEEING_ETC', 'EFFTIME_ETC',
       'TSNR2_ELG', 'TSNR2_QSO', 'TSNR2_LRG', 'TSNR2_LYA', 'TSNR2_BGS',
       'TSNR2_GPBDARK', 'TSNR2_GPBBRIGHT', 'TSNR2_GPBBACKUP',
       'LRG_EFFTIME_DARK', 'ELG_EFFTIME_DARK', 'BGS_EFFTIME_BRIGHT',
       'LYA_EFFTIME_DARK', 'GPB_EFFTIME_DARK', 'GPB_EFFTIME_BRIGHT',
       'GPB_EFFTIME_BACKUP', 'TRANSPARENCY_GFA', 'SEEING_GFA',
       'FIBER_FRACFLUX_GFA', 'FIBER_FRACFLUX_ELG_GFA',
       'FIBER_FRACFLUX_BGS_GFA', 'FIBERFAC_GFA', 'FIBERFAC_ELG_GFA',
       'FIBERFAC_BGS_GFA', 'AIRMASS_GFA', 'SKY_MAG_AB_GFA', 'SKY_MAG_G_SPEC',
       'SKY_MAG_R_SPEC', 'SKY_MAG_Z_SPEC', 'EFFTIME_GFA', 'EFFTIME_DARK_GFA',
       'EFFTIME_BRIGHT_GFA', 'EFFTIME_BACKUP_GFA')

data_schema = DataSchema()
datas_schema = DataSchema(many=True)


@app.route('/exposures')
def get_exposures():
  all_exposures = Data.query.all()
  result = datas_schema.dump(all_exposures)
  return jsonify(result)

# @app.route("/exposures/<int:id>")
# def exposure_detail(id):
#     exposure = Data.query.get(id)
#     return data_schema.dump(exposure)

# @app.route("/exposures/<int:id>/filter")
# def exposure_detail_filter(id):
#     exposure = Data.query.get(id)
#     return data_schema.dump_only(exposure)

# Define the custom command
@app.cli.command("load-data")
@click.argument("fname")
def load_data(fname):
    ''' Load data from a CSV file '''
    print ('*** Load from file: ' + fname)

    # Build the Dataframe from pandas
    df = pd.read_csv( fname )

    # Iterate and load the data     
    for row in df.itertuples(index=False):

        obj = Data(*row)
        db.session.add( obj )

    # All good, commit changes
    db.session.commit()



if __name__ == '__main__':
  app.run(debug=True)