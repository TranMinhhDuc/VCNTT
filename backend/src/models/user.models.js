import mongoose from "mongoose";

const userSchema = new mongoose.Schema(
  {
    username: {
      type: String,
      required: [true, "Username is required"],
      trim: true,
      maxLength: [50, "Username cannot exceed 50 characters"],
    },

    email: {
      type: String,
      required: [true, "Email is required"],
      unique: true,
      trim: true,
      lowercase: true,
      validate: {
        validator: function (v) {
          return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
        },
        message: (props) => `${props.value} is not a valid email!`,
      },
    },

    password: {
      type: String,
      required: [true, "Password is required"],
      minLength: [6, "Password must be at least 6 characters long"],
      maxLength: [100, "Password cannot exceed 100 characters"],
    },

    phoneNumber: {
      type: String,
      required: [true, "Phone number is required"],
      validate: {
        validator: function (v) {
          return /^[0-9]{9,15}$/.test(v); // Số điện thoại từ 9-15 chữ số
        },
        message: (props) => `${props.value} is not a valid phone number!`,
      },
    },

    firstName: {
      type: String,
      required: [true, "First name is required"],
      trim: true,
    },

    lastName: {
      type: String,
      required: [true, "Last name is required"],
      trim: true,
    },
  },
  {
    timestamps: true,
  }
);

const User = mongoose.model("User", userSchema);
export default User;
