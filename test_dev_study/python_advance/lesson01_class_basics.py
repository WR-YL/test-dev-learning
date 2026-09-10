"""
第一课：面向对象基础 - 类与对象
知识点：class 定义、__init__ 构造方法、self、实例属性、实例方法

练习任务：
    定义一个 TestCase 类，模拟测试用例的封装。
    - 属性：case_id（用例编号）、title（用例标题）、
            status（状态，默认 "未执行"）、reason（失败原因，默认 None）
    - 方法：
        run(self)              -> 打印 "正在执行用例: <case_id> <title>"
        pass_case(self)        -> 将 status 改为 "通过"
        fail_case(self, reason)-> 将 status 改为 "失败"，并记录 reason
        show_result(self)      -> 打印用例最终状态

    在 __main__ 中：
        1. 创建 2 个 TestCase 对象
        2. 分别调用 run()、pass_case() / fail_case()、show_result()
        3. 其中一条用例标记通过，另一条标记失败并填写原因
"""
class TestCase:
    # TODO: 在 __init__ 中初始化 case_id、title、status、reason
    def __init__(self, case_id, title):
      self.case_id=case_id
      self.title=title
      self.status="未执行"
      self.reason=None
      # 删除 pass，补全代码

    # TODO: 打印正在执行的用例信息
    def run(self):
        print(f"正在执行用例：{self.case_id} {self.title}")

    # TODO: 标记用例通过
    def pass_case(self):
        self.status="通过"

    # TODO: 标记用例失败，记录原因
    def fail_case(self, reason):
        self.status="失败"
        self.reason=reason

    # TODO: 打印用例最终状态
    def show_result(self):
        reason =self.reason if self.reason else "无"
        print(f"{self.case_id}|{self.title}|状态：{self.status}|失败原因：{reason}")


if __name__ == "__main__":
    # TODO: 创建用例对象并调用方法
  case1=TestCase("TC001","登录测试")
  case2=TestCase("TC002","注册测试")
  case1.run()
  case1.pass_case()
  case1.show_result()

  case2.run()
  case2.fail_case("密码错误")
  case2.show_result()


















  
