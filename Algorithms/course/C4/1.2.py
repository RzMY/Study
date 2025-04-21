# 动态规划求图像压缩问题
# 作者: 计算机202205 邱宗森 202203792

def optimal_segmentation(P):
    n = len(P)
    dp = [0] + [float('inf')] * n  # 初始化动态规划数组，dp[i]表示前i个元素的最小存储位数
    segmentation = [0] * (n + 1)   # 记录分割位置

    # 遍历每一个位置，寻找最优分割点
    for i in range(1, n + 1):
        for j in range(i):
            bits, segments = calculate_bits(P[j:i])  # 计算当前段的存储位数
            if dp[j] + bits < dp[i]:
                dp[i] = dp[j] + bits
                segmentation[i] = j  # 更新分割点

    segments = []
    i = n
    # 根据分割点重构分段方案
    while i > 0:
        segments.insert(0, P[segmentation[i]:i])
        i = segmentation[i]
    
    return segments, dp[n]

def calculate_bits(segment):
    max_val = max(segment)  # 找到当前段的最大值
    bits_per_element = max_val.bit_length()  # 计算每个元素需要的位数
    segment_bits = len(segment) * bits_per_element  # 当前段所有元素的总位数
    overhead = 11  # 每段的存储开销位数
    total_bits = segment_bits + overhead  # 当前段的总存储位数
    return total_bits, segment

def main():
    P = [10, 12, 15, 255, 1, 2]
    # P = [6, 5, 7, 5, 245, 180]
    segments, total_bits = optimal_segmentation(P)

    print("最小长度：", total_bits)
    print("共分成：", len(segments), "段")
    for idx, seg in enumerate(segments, 1):
        max_val = max(seg)  # 当前段的最大值
        bits = max_val.bit_length()  # 需要的存储位数
        print(f"第{idx}段含有{len(seg)}元素. 需要存储位数{bits}")

if __name__ == "__main__":
    main()