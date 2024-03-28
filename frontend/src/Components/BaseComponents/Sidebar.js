import React from 'react';
import './Sidebar.css';
import { Link } from 'react-router-dom';

const Sidebar = () => {
    return (
        <aside className="sidebar">
            <nav>
                <ul>
                    <li>
                        <Link to="/">
                            <span className="icon">
                                <i className="fas fa-home"></i>
                            </span>
                            || &nbsp; Home
                            <span className="arrow-icon">
                                <i className="fas fa-chevron-right"></i>
                            </span>
                        </Link>
                    </li>
                    <li>
                        <Link to="/create-product">
                            <span className="icon">
                                <i className="fas fa-plus"></i>
                            </span>
                            || &nbsp; Create
                            <span className="arrow-icon">
                                <i className="fas fa-chevron-right"></i>
                            </span>
                        </Link>
                    </li>
                    <li>
                        <Link to="/products">
                            <span className="icon">
                                <i className="fas fa-shopping-cart"></i>
                            </span>
                            || &nbsp; Products
                            <span className="arrow-icon">
                                <i className="fas fa-chevron-right"></i>
                            </span>
                        </Link>
                    </li>
                    <li>
                        <Link to="/about">
                            <span className="icon">
                                <i className="fas fa-info-circle"></i>
                            </span>
                            || &nbsp; About
                            <span className="arrow-icon">
                                <i className="fas fa-chevron-right"></i>
                            </span>
                        </Link>
                    </li>
                    <li>
                        <Link to="/contact">
                            <span className="icon">
                                <i className="fas fa-envelope"></i>
                            </span>
                            || &nbsp; Contact
                            <span className="arrow-icon">
                                <i className="fas fa-chevron-right"></i>
                            </span>
                        </Link>
                    </li>
                    
                    <div className="auth_btn">
                        <hr/>
                        <hr/>
                        <hr/>
                        <li>
                            <Link to="/sign-up">
                                <span className="icon">
                                    <i className="fas fa-user-plus"></i>
                                </span>
                                Register
                            </Link>
                        </li>
                        <hr/>
                        <hr/>
                        <hr/>
                    </div>
                </ul>
            </nav>
        </aside>
    );
}

export default Sidebar;
