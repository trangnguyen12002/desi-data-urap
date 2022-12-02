import { Box } from "@mui/material";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { ColorModeContext, tokens } from "../../theme";
import Header from "../../components/Header";
import { useTheme } from "@mui/material";
import React, { useState, useEffect, useContext } from "react";
import LightModeOutlinedIcon from '@mui/icons-material/LightModeOutlined';
import DarkModeOutlinedIcon from '@mui/icons-material/DarkModeOutlined';
import { IconButton } from "@mui/material";



const Exposures = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const colorMode = useContext(ColorModeContext); 

  const columnNames = ['NIGHT', 'EXPID', 'TILEID', 'TILERA', 'TILEDEC', 'MJD', 'SURVEY',
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
  'EFFTIME_BRIGHT_GFA', 'EFFTIME_BACKUP_GFA']

  const columns = columnNames.map((key, id) => {
    if (['SURVEY', 'PROGRAM', 'FAPRGRM', 'FAFLAVOR','GOALTYPE'].includes(key)) {
        return {
            field: key,
            headerName: key,
            width: 160,
            type: "string",
        };
    }
    if (['NIGHT'].includes(key)) {
        return {
            field: key,
            headerName: key,
            width: 160,
            type: "dateTime",
            valueGetter: ({ value }) => value && new Date(value),
        };
    }
    return {
        field: key,
        headerName: key,
        width: 160,
        type: "number",
    };
  });

  const [data, setdata] = useState([]);
  const [loading, setLoading] = useState(true);

  // Using useEffect for single rendering
  useEffect(() => {
    // Using fetch to fetch the api from 
    // flask server it will be redirected to proxy
    fetch("http://127.0.0.1:5000/exposures").then((res) =>
        res.json().then((data) => {
            // Setting a data from api
            console.log(data)
            setdata(data);
        }).finally(() => setLoading(false))
    );
  }, []);

return (
    <Box m="20px">
    <Box display='flex' justifyContent='space-between' p={2}>
        <Header
            title="Dark Energy Spectroscopic Instrument @ UC Berkeley"
            subtitle="List of exposures"
        />
         <Box display='flex'>
                <IconButton onClick={colorMode.toggleColorMode}>
                    {theme.palette.mode === 'dark' ? (
                        <DarkModeOutlinedIcon />
                    ) : (
                        <LightModeOutlinedIcon />
                    )}
                </IconButton>
            </Box>
    </Box>
    <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
        "& .MuiDataGrid-root": {
            border: "none",
        },
        "& .MuiDataGrid-cell": {
            borderBottom: "none",
        },
        "& .name-column--cell": {
            color: colors.greenAccent[300],
        },
        "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
        },
        "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
        },
        "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
        },
        "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
        },
        "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
            color: `${colors.grey[100]} !important`,
        },
        }}
    >
        { !loading && 
        <DataGrid
            checkboxSelection 
            rows={data}
            columns={columns}
            components={{ Toolbar: GridToolbar }}
            getRowId={(row) => row?.EXPID}
        />}
    </Box>  
    </Box>
);
};

export default Exposures;