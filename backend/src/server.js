import express from 'express';
import {PORT} from './config/env.js';
import cors from 'cors';
import authRoute from './Routes/auth.route.js';
import dbConnect from './config/DbConnection.config.js';

const app = express();
dbConnect();

app.use(cors({
    origin:'http://localhost:5001/',
    credentials: true
}));

app.use(express.json());

app.use('/api/v1/auth', authRoute)
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
})