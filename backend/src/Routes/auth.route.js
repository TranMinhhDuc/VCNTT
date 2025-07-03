import { Router } from "express";
import User from "../models/user.models.js";
import mongoose from "mongoose";
import bcrypt from 'bcrypt';


const authRoute = Router();

authRoute.use('/user', async (req, res) => {
    try {
        const users = await User.find();

        res.status(200).json({
            success: true,
            message: 'get users successfully',
            data: users
        })
    } catch (error) {
        req.statusCode(500).json({
            success: false,
            message: 'get user false'
        })
    }
});

authRoute.post('/register', async (req, res) =>{
    const session = await mongoose.startSession();
    await session.startTransaction();
    
    try {
        const {
            firstName,
            lastName,
            username,
            password,
            email,
            phoneNumber
        } = req.body;

        const existsUsername = await User.findOne({ username });
        const existsEmail = await User.findOne({ email });
        const existsPhoneNumber = await User.findOne({ phoneNumber });

        if(existsEmail || existsPhoneNumber || existsUsername) {
            const error = new Error();
            throw error;
        }

        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        const newUser = new User({
            firstName,
            lastName,
            username,
            password: hashedPassword,
            email,
            phoneNumber
        });

        await newUser.save({session});

        await session.commitTransaction();
        await session.endSession();

        res.status(201).json({
            success: true,
            message: "User is created successfully",
            data: {
                user: newUser
            }
        });

    } catch (error) {
        (await session).abortTransaction();
        session.endSession();
        res.status(500).json({
            success: false,
            message: 'register false'
        })
    }
});

authRoute.put('/update-user', async (req, res) => {
    const session = await mongoose.startSession();
    await session.startTransaction();

    try {
        const {
            firstName,
            lastName,
            username,
            password,
            email,
            phoneNumber,
            id
        } = req.body;

        const existingUser = await User.findById(id).session(session);
        if (!existingUser) {
            await session.abortTransaction();
            session.endSession();
            return res.status(404).json({
                success: false,
                message: 'User not found'
            });
        }

        // Kiểm tra nếu có username/email/phoneNumber trùng với người khác
        const existsUsername = await User.findOne({ username, _id: { $ne: id } }).session(session);
        const existsEmail = await User.findOne({ email, _id: { $ne: id } }).session(session);
        const existsPhoneNumber = await User.findOne({ phoneNumber, _id: { $ne: id } }).session(session);

        if (existsUsername || existsEmail || existsPhoneNumber) {
            const error = new Error();
            throw error;
        }

        // Cập nhật thông tin
        existingUser.firstName = firstName;
        existingUser.lastName = lastName;
        existingUser.username = username;
        existingUser.email = email;
        existingUser.phoneNumber = phoneNumber;

        if (password) {
            const salt = await bcrypt.genSalt(10);
            existingUser.password = await bcrypt.hash(password, salt);
        }

        await existingUser.save({ session });

        await session.commitTransaction();
        session.endSession();

        res.status(200).json({
            success: true,
            message: 'User updated successfully',
            data: existingUser
        });

    } catch (error) {
        await session.abortTransaction();
        session.endSession();
        res.status(500).json({
            success: false,
            message: 'Update failed',
            error: error.message
        });
    }
});


export default authRoute;