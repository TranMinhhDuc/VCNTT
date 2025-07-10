import React, { createContext, useState } from "react";

export const AdminContext = createContext();

const initialState = {
    accessToken: localStorage.getItem('accessToken') || null
};

const AdminContextProvider = ({ children }) => {
    const [accessToken, setAccessToken] = useState(initialState.accessToken);
    const [showSidebar, setShowSidebar] = useState(true);

    const resetContext = () => {
        setAccessToken(null);
        localStorage.removeItem("accessToken");
    };

    const value = {
        accessToken, setAccessToken,
        resetContext, 
        showSidebar, setShowSidebar
    };

    return (
        <AdminContext.Provider value={value}>
            {children}
        </AdminContext.Provider>
    );
};

export default AdminContextProvider;
