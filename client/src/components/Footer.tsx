import React from 'react';
import { FaGithub, FaLinkedin } from "react-icons/fa";

const Footer = () => {
  return (
    <footer className="bg-blue-700 border-b border-blue-500">
      <div className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
        <div className="flex h-20 items-center justify-between">
          <div className="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
            {/* Your other footer content */}
          </div>
          <div className="flex flex-1 justify-end">
            <div className="flex">
              <a href="https://github.com/rickylin1" target="_blank" rel="noopener noreferrer">
                <FaGithub className="h-10 w-auto text-gray-800" />
              </a>
              <a href="https://www.linkedin.com/in/ricky-lin1" target="_blank" rel="noopener noreferrer" className="ml-4">
                <FaLinkedin className="h-10 w-auto text-gray-800" />
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
