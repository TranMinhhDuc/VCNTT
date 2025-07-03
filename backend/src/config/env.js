import dotenv from 'dotenv';

dotenv.config({ path: './.env' });


const PORT = process.env.PORT;
const DB_URL = process.env.DB_URL;

const JWT_SECRET = process.env.JWT_SECRET;
const JWT_EXPIRES_IN = process.env.JWT_EXPIRES_IN;

export {
    PORT,
    DB_URL,
    JWT_SECRET,
    JWT_EXPIRES_IN
}