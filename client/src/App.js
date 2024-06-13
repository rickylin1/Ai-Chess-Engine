import {Route, createBrowserRouter, createRoutesFromElements, RouterProvider} from 'react-router-dom'
import Homepage from './pages/Homepage.tsx';
import NotFoundPage from './pages/NotFoundPage.tsx';
import MainLayout from './Layouts/MainLayout.tsx';
import Ai from './pages/ai.tsx';
import Player from './pages/player.tsx';

function App() {

  const router = createBrowserRouter(
    createRoutesFromElements(
    <Route path = "/" element = {<MainLayout></MainLayout>}> 
      <Route index element = {<Homepage></Homepage>}/> 
      <Route path = '/ai' element = {<Ai></Ai>}/> 
      <Route path = '/player' element = {<Player></Player>}/> 
      <Route path = '*' element = {<NotFoundPage/>}/>
    </Route>
   
  )
  )

  return (
    <>
      <RouterProvider router = {router}></RouterProvider>
    </>
  );
}

export default App;