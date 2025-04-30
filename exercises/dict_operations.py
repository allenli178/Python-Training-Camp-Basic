"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""


def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作

    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数

    返回:
    - 根据操作返回不同结果
    """
    # 请在下方编写代码
    if operation == "add":
        # args[0] 是要添加的学生姓名，args[1] 是成绩
        students_dict[args[0]] = args[1]
        return students_dict

    elif operation == "remove":
        # args[0] 是要删除的学生姓名
        if args[0] in students_dict:
            del students_dict[args[0]]
        return students_dict

    elif operation == "update":
        # args[0] 是要更新的学生姓名， args[1] 是新的成绩
        if args[0] in students_dict:
            students_dict[args[0]] = args[1]
        return students_dict

    elif operation == "get":
        # args[0] 是查询的学生姓名
        return students_dict.get(args[0], None)

    else:
        raise ValueError("Unsupported operation")
