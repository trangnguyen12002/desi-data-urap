import { ColorModeContext, useMode } from './theme'; 
import { CssBaseline, ThemeProvider } from "@mui/material";
import Sidebar from './scenes/global/Sidebar';
import { Routes, Route } from 'react-router-dom'; 
import Exposures from "./scenes/exposures";


function App() {
  const [theme, colorMode] = useMode(); 
  // const [isSidebar, setIsSidebar] = useState(true);


  return (
    <ColorModeContext.Provider value = {colorMode}>
      <ThemeProvider theme = {theme}> 
        <CssBaseline />
        <div className="app">
        <Sidebar />
          <main className="content">
            <Routes>
              <Route path="/" element={<Exposures />} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
