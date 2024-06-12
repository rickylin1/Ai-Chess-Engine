import React from 'react';
import { NavLink } from 'react-router-dom';
import logo from '../assets/chessicon.svg';

const NavBar = () => {
  const linkClass = ({ isActive }) =>
    isActive
      ? 'text-white bg-black hover:bg-gray-900 hover:text-white rounded-md px-3 py-2'
      : 'text-white hover:bg-gray-900 hover:text-white rounded-md px-3 py-2';

  return (
    <nav className="bg-blue-700 border-b border-blue-500">
      <div className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
        <div className="flex h-20 items-center justify-between">
          <div className="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
            {/* Logo */}
            <NavLink className="flex flex-shrink-0 items-center" to="/">
              <img className="h-10 w-auto pr-3" src={logo} alt="React Jobs" />
              <span className="hidden md:block text-white text-2xl font-bold ml-2">
                NotSoDeepBlue
              </span>
            </NavLink>
            <div className="md:ml-auto flex items-center space-x-2 h-full">
              <NavLink to="/" className={linkClass}>
                Home
              </NavLink>
              <NavLink to="/player" className={linkClass}>
                2 Player
              </NavLink>
              <NavLink to="/ai" className={linkClass}>
                AI
              </NavLink>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
