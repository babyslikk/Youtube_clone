// General Imports
import { Routes, Route } from "react-router-dom";
import DisplayComment from "./components/DisplayComment/DisplayComment";
import SearchBar from "./components/SearchBar/SearchBar";
import React, { useState } from 'react';

import "./App.css";
// import { DATA } from "./localData";

// Pages Imports
import HomePage from "./pages/HomePage/HomePage";
import LoginPage from "./pages/LoginPage/LoginPage";
import RegisterPage from "./pages/RegisterPage/RegisterPage";
import VideoPage from "./pages/VideoPage/VideoPage";
import YouTubePage from "./pages/YouTubePage/YouTubePage";
import SearchPage from "./pages/SearchPage/SearchPage";






// Component Imports
import Navbar from "./components/NavBar/NavBar";
import Footer from "./components/Footer/Footer";



// Util Imports
import PrivateRoute from "./utils/PrivateRoute";

function App() {
  const [commentId, setCommentId] = useState(['Id']);



  return (
    
    <div>
      <Navbar />
      <Routes>
        <Route
          path="/"
          element={
            <PrivateRoute>
              <HomePage />
            </PrivateRoute>
          }
        />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/home" element={<YouTubePage />} />
        <Route path="/video/:videoid" element={<VideoPage />} />
        <Route path="/search/:search" element={<SearchPage />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;