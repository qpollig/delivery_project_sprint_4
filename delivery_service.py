# 21 ноя 2023, 13:05:50 98251862	OK 48ms 4.26Mb
import sys


def count_platforms():
    """Определяет минимальное количество транспортных платформ,
    необходимое для перевозки всех роботов, описанных в массиве."""
    arr_str: list[str] = sys.stdin.readline().rstrip().split()
    limit: int = int(sys.stdin.readline().rstrip())
    arr: list[int] = [int(i) for i in arr_str]
    arr.sort()
    count: int = 0
    left: int = 0
    right: int = len(arr) - 1
    while left <= right:
        if arr[left] + arr[right] <= limit:
            count += 1
            left += 1
            right -= 1
        else:
            count += 1
            right -= 1
    return count


if __name__ == '__main__':
    print(count_platforms())
