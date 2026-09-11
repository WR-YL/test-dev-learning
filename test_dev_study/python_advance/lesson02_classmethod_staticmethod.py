"""
第二课：类方法与静态方法（@classmethod / @staticmethod）
知识点：@classmethod、@staticmethod、cls、类属性、工厂方法

回顾第一课：
    实例方法第一个参数是 self，能访问实例属性。
    本课学习另外两种方法：
    - 类方法 @classmethod：第一个参数是 cls（类本身），常用于工厂方法
    - 静态方法 @staticmethod：没有 self/cls，是挂在类下的工具函数

练习任务：
    在第一课 TestCase 类基础上扩展，新增：
    1. 类属性 total_count：记录一共创建了多少个用例对象（每次 __init__ 时 +1）
    2. from_dict(cls, data) [类方法]：从字典创建 TestCase 对象
       - 输入 {"case_id": "TC001", "title": "登录测试"}
       - 返回 TestCase 实例
       - 这是工厂方法：不用 TestCase(...) 直接造，而是从字典造
    3. generate_case_id(prefix) [静态方法]：生成用例编号
       - 输入 "TC"，返回 "TC_0001"（用 total_count 拼接，格式 TC_0001）
       - 提示：可用 f"{prefix}_{cls.total_count:04d}"，但注意这是静态方法没有 cls
       - 改用从外部传入的计数，或直接用类名访问 TestCase.total_count
    4. show_total_count(cls) [类方法]：打印当前用例总数
       - 通过 cls.total_count 访问类属性

    在 __main__ 中：
        1. 用 from_dict 批量从字典列表创建 3 个用例对象
        2. 用 generate_case_id 演示生成编号
        3. 调用 show_total_count 打印总数
"""


class TestCase:
    # TODO: 类属性 total_count，初始值 0（写在 class 内、方法外）
    # 提示：total_count = 0

    def __init__(self, case_id, title):
        self.case_id = case_id
        self.title = title
        self.status = "未执行"
        self.reason = None
        # TODO: 每次创建对象时 total_count +1
        # 提示：TestCase.total_count += 1（用类名访问类属性）

    def run(self):
        print(f"正在执行用例：{self.case_id} {self.title}")

    def pass_case(self):
        self.status = "通过"

    def fail_case(self, reason):
        self.status = "失败"
        self.reason = reason

    def show_result(self):
        reason = self.reason if self.reason else "无"
        print(f"{self.case_id} | {self.title} | 状态：{self.status} | 原因：{reason}")

    # TODO: 类方法 - 从字典创建对象（工厂方法）
    @classmethod
    def from_dict(cls, data):
        # 提示：cls(...) 等价于 TestCase(...)，但用 cls 更通用
        # 提示：从 data 取 case_id 和 title
        pass  # 删除 pass，返回 cls(data["case_id"], data["title"])

    # TODO: 静态方法 - 生成用例编号
    @staticmethod
    def generate_case_id(prefix):
        # 提示：用 TestCase.total_count 拼接，格式 {prefix}_0001
        # 提示：f"{prefix}_{TestCase.total_count:04d}"
        pass  # 删除 pass，return 拼接结果

    # TODO: 类方法 - 打印用例总数
    @classmethod
    def show_total_count(cls):
        # 提示：cls.total_count 访问类属性
        pass  # 删除 pass，打印总数


if __name__ == "__main__":
    # TODO: 用 from_dict 批量创建用例
    cases_data = [
        {"case_id": "TC001", "title": "登录测试"},
        {"case_id": "TC002", "title": "注册测试"},
        {"case_id": "TC003", "title": "搜索测试"},
    ]
    # 提示：cases = [TestCase.from_dict(item) for item in cases_data]
    #       这叫列表推导式，遍历 cases_data，每项调 from_dict 生成对象

    # TODO: 演示 generate_case_id
    # 提示：new_id = TestCase.generate_case_id("TC")

    # TODO: 调用 show_total_count
    # 提示：TestCase.show_total_count()

    # TODO: 让每条用例跑一下并 show_result
    pass
