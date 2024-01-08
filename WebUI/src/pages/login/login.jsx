import { Button } from "antd";
import { useNavigate } from "react-router-dom";
import "./login.css";

export const Login = () => {
  const navigate = useNavigate();

  const handleLogin = () => {
    // Perform your login logic here (e.g., API calls)
    // If successful, set a flag or token indicating authentication
    localStorage.setItem("isLoggedIn", true); // Example storage
    navigate("/config");
  };

  return (
    <>
      <h3>Login Page!</h3>
      <Button onClick={handleLogin}>Login</Button>
    </>
  );
};
