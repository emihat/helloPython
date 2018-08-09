# -*- coding: utf-8 -*-

items = ["A", "T", "G", "C"]
values = [1] * len(items)

data = [
        ["C", "T", "A", "G"],
        ["", "", "T", "C"],
        ["", "C", "G", "T"],
        ["T", "G", "C", "A"],
        ]

trial_cnt = 0

# 行と列のサーチを10回繰り返したらやめる
while trial_cnt <= 10:
    trial_cnt += 1
    emptycel_cnt = 0

    for i, row in enumerate(data):
        for j, cel in enumerate(row):

            # 値が入っているセルは検索しない
            if cel != "":
                continue

            emptycel_cnt += 1

            # 同じ行にある値をチェック
            tmp_row = dict(zip(items, values))
            for j2, cel2 in enumerate(row):
                if j == j2 or cel2 == "":
                    continue
                del tmp_row[cel2]

            # 同じ列にある値をチェック
            tmp_col = dict(zip(items, values))
            for i2, row2 in enumerate(data):
                cel3 = row2[j]
                if i == i2 or cel3 == "":
                    continue
                del tmp_col[cel3]

            # 行と列で一つの値に絞ることができればその値を入力
            candidates = []
            for tmp_val in tmp_row.keys():
                if tmp_val in tmp_col:
                    candidates.append(tmp_val)
                    if len(tmp_val) == 1:
                        data[i][j] = tmp_val

    # 空のセルが無くなったらやめる
    if emptycel_cnt == 0:
        break

# final answer
for row in data:
    print("|" + "|".join(row) + "|")