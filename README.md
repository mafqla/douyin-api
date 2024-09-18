
# Douyin API

## 简介
本项目提供了用于获取抖音平台用户及视频信息的API接口，方便开发者获取用户作品、收藏、喜欢、观看历史等数据。

## 安装依赖
请先确保你的环境已经安装了 `pip`，然后运行以下命令安装本项目所需的所有依赖项：

```shell
pip install -r requirements.txt
```

## 导出依赖
如果你需要将本项目的依赖导出到 `requirements.txt`，可以使用以下命令：

```shell
pip freeze > requirements.txt
```

## 接口文档
详细的接口文档已在 `docs` 文件夹中提供。你可以通过以下链接查看：

- [用户信息接口文档](./docs/user-api.md)
- [视频接口文档](./docs/video-api.md)

## 使用方法
请参照对应的接口文档，按照说明进行API调用。
使用前，会弹出输入cookie，请从douyin的网页的接口复制cookie后输入，会自动生成config文件夹。

## 文件结构
```text
├── README.md         # 项目简介及使用说明
├── requirements.txt  # 项目依赖文件
├── docs              # 文档目录
│   ├── user-api.md   # 用户信息相关接口文档
│   └── video-api.md  # 视频相关接口文档
├── api               # 接口文件目录
│   └── ...           # 接口相关代码文件
├── utils             # 工具类目录
│   └── ...           # 工具类函数代码
├── tests             # 测试目录
│   └── ...           # 测试代码
├── config            # 配置文件目录
│   └── cookie.json   # 存储cookie的配置文件
├── app.py            # 启动文件

```

## 贡献
欢迎提交问题或贡献代码。