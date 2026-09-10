# python_advance - Python 进阶练习

本模块记录 Python 进阶知识点实操，循序渐进覆盖：面向对象、装饰器、yaml 配置读取。

---

## 第一课：面向对象基础 - 类与对象

### 知识点
- `class` 关键字：定义一个类（类 = 模板 / 蓝图，描述一类事物的属性与行为）。
- `__init__` 构造方法：创建对象时自动调用，用于初始化实例属性。
- `self`：指向当前对象实例本身，通过 `self.属性名` 访问 / 设置实例属性。
- 实例属性：每个对象各自持有，互不影响。
- 实例方法：定义在类里的函数，第一个参数永远是 `self`。

### 文件说明
- `lesson01_class_basics.py`：本课练习模板，含 `TestCase` 类骨架与 TODO 注释，需手动补全。

### 运行命令
```bash
cd test_dev_study/python_advance
python lesson01_class_basics.py
```

### 代码说明
练习用面向对象方式封装一个「测试用例」对象：
- `__init__(self, case_id, title)` 初始化用例编号、标题、状态（默认 `未执行`）、失败原因（默认 `None`）。
- `run()` 打印正在执行哪条用例。
- `pass_case()` / `fail_case(reason)` 修改用例状态。
- `show_result()` 打印用例最终状态。

在 `__main__` 中创建 2 个用例对象，模拟一条通过、一条失败，打印结果。
