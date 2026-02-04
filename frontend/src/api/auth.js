import axiosClient from "./axiosClient";

const authApi = {
  register: (data) => {
    // data gồm: { username, password, email }
    return axiosClient.post("/auth/register", data);
  },

  login: (data) => {
    // data gồm: { username, password }
    return axiosClient.post("/auth/login", data);
  },

  // Hàm tiện ích để lấy token từ LocalStorage
  getToken: () => localStorage.getItem("access_token"),

  // Hàm đăng xuất
  logout: () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("user_info");
  },
};

export default authApi;
