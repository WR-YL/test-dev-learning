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

---

## 第二课：类方法与静态方法（@classmethod / @staticmethod）

### 知识点
- **实例方法**（第一课学的）：第一个参数是 `self`，能访问实例属性。调用方式 `对象.方法()`。
- **类方法** `@classmethod`：第一个参数是 `cls`（类本身，不是实例），能访问/修改类级别的数据。常用场景是**工厂方法**——提供另一种创建对象的方式。
- **静态方法** `@staticmethod`：没有 `self` 也没有 `cls`，就是个挂在类下面的普通函数。用于和类逻辑相关、但不需要访问实例/类数据的工具方法。
- 三者对比：
  | 方法类型 | 装饰器 | 第一个参数 | 能访问实例属性？ | 能访问类属性？ | 典型用途 |
  |---------|--------|-----------|----------------|---------------|---------|
  | 实例方法 | 无 | `self` | ✅ | ✅ | 操作单个对象 |
  | 类方法 | `@classmethod` | `cls` | ❌ | ✅ | 工厂方法/替代构造 |
  | 静态方法 | `@staticmethod` | 无 | ❌ | ❌ | 工具函数 |

### 文件说明
- `lesson02_classmethod_staticmethod.py`：本课练习模板，扩展第一课的 `TestCase` 类，新增类方法和静态方法。

### 运行命令
```bash
cd test_dev_study/python_advance
python lesson02_classmethod_staticmethod.py
```

### 代码说明
在第一课 `TestCase` 基础上扩展：
- `from_dict(cls, data)`（类方法）：从字典批量创建用例对象，典型工厂方法。
  - 输入示例：`{"case_id": "TC001", "title": "登录测试"}`
  - 返回一个 `TestCase` 实例。
- `generate_case_id(prefix)`（静态方法）：根据前缀生成用例编号，如 `generate_case_id("TC")` 返回 `"TC_0001"`。不需要访问实例或类数据，所以用静态方法。
- `show_total_count()`（类方法）：打印当前一共创建了多少个用例对象（用类属性计数）。
