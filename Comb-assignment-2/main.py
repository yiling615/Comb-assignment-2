import time
# 从 tsp.py 导入所有需要的函数和常量
from tsp import backtracking, minout, two_minout, brute_force_tsp, inf

def main():
    # 教师示例中的 5x5 邻接矩阵
    graph = [
        [inf, 1, 3, 5, 8],
        [1, inf, 4, 2, 9],
        [3, 4, inf, 7, 2],
        [5, 2, 7, inf, 2],
        [8, 9, 2, 2, inf]
    ]

    # 打印表头，增加 brute 这一行
    print(f"{'alg':<10} | {'cost':<5} | {'tour':<25} | {'elapsed time':<15}")
    print("-" * 65)

    # --- 1. 测试暴力算法 (Brute Force) ---
    start_bf = time.time()
    res_bf = brute_force_tsp(graph)
    end_bf = time.time()
    tour_bf = "->".join([chr(65 + i) for i in res_bf[1]])
    print(f"{'brute':<10} | {res_bf[0]:<5} | {tour_bf:<25} | {end_bf - start_bf:.4f}s")

    # --- 2. 测试回溯算法 + minout ---
    start_minout = time.time()
    res_minout = backtracking(graph=graph, path=[0], shortest=inf, best_path=[], bounding=minout)
    end_minout = time.time()
    tour_minout = "->".join([chr(65 + i) for i in res_minout[1]])
    print(f"{'minout':<10} | {res_minout[0]:<5} | {tour_minout:<25} | {end_minout - start_minout:.4f}s")

    # --- 3. 测试回溯算法 + mintwo (two_minout) ---
    start_min2 = time.time()
    res_min2 = backtracking(graph=graph, path=[0], shortest=inf, best_path=[], bounding=two_minout)
    end_min2 = time.time()
    tour_min2 = "->".join([chr(65 + i) for i in res_min2[1]])
    print(f"{'mintwo':<10} | {res_min2[0]:<5} | {tour_min2:<25} | {end_min2 - start_min2:.4f}s")

    # --- 按照老师要求的格式输出最终结果 ---
    print("\n" + "="*50)
    # 再次运行以获取结果对象（或直接复用 res_minout）
    result = backtracking(graph=graph, path=[0], shortest=inf, best_path=[], bounding=minout)
    print(f"TSP({graph}) = {result}")

if __name__ == "__main__":
    main()
"""from math import inf
import tsp

def main():

    # graph = [
    #         [inf, 1, 3, 2],
    #         [1, inf, 1, 2],
    #         [3, 1, inf, 5],
    #         [2, 2, 5, inf]
    #     ]

    graph = [
            [0, 2,   3,   8],
            [2, 0,   inf, 7],
            [3, inf, 0,   1],
            [8, 7,   1,   0]
        ]

    result = tsp.backtracking(graph=graph, bounding = tsp.minout)

    print(f'TSP({graph}) = {result}')

if __name__ == "__main__":
    main()"""