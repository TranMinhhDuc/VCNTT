import mongoose from "mongoose";
import { DB_URL } from "./env.js";

const dbConnect = async () => {
    try {
        console.log(DB_URL);
        const connection = await mongoose.connect(DB_URL);
        console.log("Database connected successfully:", connection.connection.host);
    } catch (error) {
        console.error("Database connection failed:", error.message);
        process.exit(1); 
    }

};

export default dbConnect;