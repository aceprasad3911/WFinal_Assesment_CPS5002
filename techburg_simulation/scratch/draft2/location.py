# location.py
class Location:
    def __init__(self, x: int, y: int) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Coordinates must be integers.")
        if x < 0 or y < 0:
            raise ValueError("Coordinates must be non-negative.")

        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def set_x(self, new_x: int) -> None:
        if not isinstance(new_x, int) or new_x < 0:
            raise ValueError("New x-coordinate must be a non-negative integer.")
        self.__x = new_x

    def set_y(self, new_y: int) -> None:
        if not isinstance(new_y, int) or new_y < 0:
            raise ValueError("New y-coordinate must be a non-negative integer.")
        self.__y = new_y