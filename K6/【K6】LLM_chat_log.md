# 【K6】文件和函数 -- AI对话记录

## 第2题：写入和读出小抄

**我**：我在做"跳过7游戏"，需要把游戏小抄写入 skip7tips.dat，再读取打印。能给个思路吗？不要直接写代码。

**AI**：好的，给你思路：
1. 小抄本质就是"被跳过的数字"——能被7整除或包含数字7的数。在原跳过7游戏的循环里，被跳过的分支用 `tips.append(i)` 收集起来。
2. 写文件用 `open('skip7tips.dat', 'w', encoding='utf-8')`，遍历 tips 列表，每个数字写一行（加 `'\n'`）。
3. 读文件用 `open('skip7tips.dat', 'r')`，`f.read().split()` 按空白分割成列表后打印。
4. 关键点：用 `with` 语句自动关闭文件；判断"包含7"用 `'7' not in str(i)`。

---

## 第3题：分段复制文件

**我**：大文件无法一次读入内存，怎么分段复制？题目提示了 `f.seek(0, 2)`。

**AI**：思路如下：
1. 用 `'rb'` 二进制模式打开源文件（大文件要按字节处理）。
2. `f.seek(0, 2)` 把指针移到文件尾，**返回值就是文件总字节数**，记为 `total_size`。
3. `f.seek(0)` 把指针移回开头。
4. 设个 `chunk_size`（比如 1024），循环 `while copied < total_size`：每次 `chunk = f_src.read(chunk_size)` 读一段，`f_dst.write(chunk)` 写一段，`copied += len(chunk)`。
5. 目标文件用 `'wb'` 打开。验证复制是否成功：比较两文件大小用 `os.path.getsize()`。

---

## 第8题：调整分词

**我**：jieba 默认分词不符合期望，怎么调整？

**AI**：
1. 先 `jieba.lcut(sentence)` 看默认结果，对比你的期望。
2. `jieba.add_word("词")` —— 把某词加入词典，让它被识别为整体。
3. `jieba.del_word("词")` —— 把某词从词典删除，避免它被组合。
4. 比如想把"销售部长"当整体就 `add_word("销售部长")`；想让"部长会"成词就 `del_word("销售部长")` + `add_word("部长会")`。
5. 分三次展示：默认 → 方式一 → 方式二，对比差异。

---

## 第9题：前20高频词

**我**：怎么对比不同诗人的高频词？数据是全唐诗.txt。

**AI**：
1. **解析**：用正则 `卷\d+_\d+\s*【.*?】(\S+)` 匹配标题行，提取作者名；后续非空行累加到该作者名下（字典 `{作者: 文本}`）。
2. **分词**：`jieba.lcut(text)`，过滤掉：单字（`len(w)>=2`）、标点（用 `re.search(r'[\u4e00-\u9fff]', w)` 确保含汉字）、停用词。
3. **统计**：`collections.Counter.most_common(20)` 取前20。
4. **对比**：选李白、杜甫、白居易、王维四位，分别输出，观察风格差异。

---

## 第13题：JSON格式

**我**：给歌曲信息加"歌词"条目，每行歌词是一个字符串，JSON怎么写？

**AI**：
1. JSON 用**数组** `[]` 存多行歌词，数组里每个元素是一行歌词的字符串。
2. 键名和字符串值都用**双引号**，最后一项不加逗号。
3. 用 Python 的话：`{"歌词": ["第一行", "第二行", ...]}`，字典对应 JSON 对象，列表对应 JSON 数组。
4. 用 `json.dumps(song, ensure_ascii=False, indent=2)` 序列化看格式，`json.dump()` 写文件，`json.load()` 读回验证。

---

## 第19题：奇偶数函数

**我**：`parity()` 函数带一个选项参数，怎么设计？

**AI**：
1. "选项参数" = 带默认值的关键字参数，如 `def parity(n, style="中文")`。
2. 判断奇偶：`n % 2 == 0` 为偶数，否则奇数。
3. `style` 选项控制输出形式："中文"打印"奇数/偶数"，"英文"打印"odd/even"等。
4. 调用时：`parity(7)` 省略选项用默认；`parity(7, style="英文")` 指定选项。

---

## 第25题：避免副作用

**我**：怎么用 `order[:]` 切片拷贝验证副作用消失？

**AI**：
1. 先写有副作用的函数 `my_order2(order)`，里面用 `order.append()`、`order[0]=...` 原地修改。
2. **有副作用**：`my_order2(order)` 调用后，外部 `order` 被改了。
3. **无副作用**：`my_order2(order[:])` 传切片拷贝，函数改的是副本，原 `order` 不变。
4. 验证原理：`order is order[:]` 为 `False`，说明切片创建了新对象；`id()` 也不同。

---

## 第9题（补充）：jieba 安装问题

**我**：导入 jieba 报 `ModuleNotFoundError`，怎么装？

**AI**：默认 pip 源可能被拦，用清华镜像：
`python -m pip install jieba -i https://pypi.tuna.tsinghua.edu.cn/simple`
装完用 `python -c "import jieba; print(jieba.__version__)"` 验证。
