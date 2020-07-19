import requests

API_URL = "https://api.maxmines.com"


class MaxMinesPython(object):
    def __init__(self, secret_key):

        self._headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MaxMinesClient/1.0.0; http://maxmines.com)",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        if len(secret_key) != 40:
            raise ValueError("Secret key phải dài 40 ký tự")

        self.secret_key = secret_key

    def get(self, path, params={}):
        """
        Method GET

        :param str path: route muốn truy cập
        :param dict params: thông số URL bạn muốn gửi tới máy chủ MaxMines
        """
        params.update(secret=self.secret_key)

        try:
            res = requests.get(MaxMinesPython.build_url(path), params=params, headers=self._headers).json()
        except requests.exceptions.ConnectionError:
            res = "Cú pháp không hợp lệ, vui lòng đọc kỹ tài liệu"
            pass

        return res

    def post(self, path, data={}):
        """
        Method POST

        :param str path: route muốn truy cập
        :param dict data: data bạn muốn gửi tới máy chủ MaxMines
        """
        data.update(secret=self.secret_key)

        try:
            res = requests.post(MaxMinesPython.build_url(path), data=data, headers=self._headers).json()
        except requests.exceptions.ConnectionError:
            res = "Cú pháp không hợp lệ, vui lòng đọc kỹ tài liệu"
            pass

        return res

    @staticmethod
    def build_url(route):
        """
        Build URL từ URL mặc định được cung cấp bởi maxmines.

        :param str route: route muốn truy cập
        :param dict params: Thông số URL bạn muốn gửi tới máy chủ MaxMines
        """
        return API_URL + route


if __name__ == "__main__":
    pass
