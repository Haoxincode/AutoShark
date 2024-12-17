from autosar_data import AutosarModel, AutosarVersion, ArxmlFile

def check_arxml_version_compatibility(file_path: str, target_version: AutosarVersion):
    # 创建 AutosarModel 实例
    model = AutosarModel()
    
    # 加载 arxml 文件
    arxml_file, errors = model.load_file(file_path)

    # 检查版本兼容性
    compatibility_errors = arxml_file.check_version_compatibility(target_version)

    # 打印结果
    if not compatibility_errors:
        print(f"The file '{file_path}' is compatible with version {target_version}.")
    else:
        print(f"The file '{file_path}' has compatibility issues with version {target_version}:")
        for error in compatibility_errors:
            print(f"- {error.element} has an issue with attribute '{error.attribute}'. Allowed versions: {error.allowed_versions}")

# 示例用法
file_path = 'window.arxml'  # 替换为实际文件路径
target_version = AutosarVersion.AUTOSAR_00047  # 替换为所需的目标版本

check_arxml_version_compatibility(file_path, target_version)