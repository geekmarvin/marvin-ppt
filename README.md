# marvin-ppt

从同一个仓库一次安装两套 Codex Skill，用于制作可编辑的 PowerPoint。

- **ppt-master** 是 Hugo He 的官方 PowerPoint 制作 Skill。这个包带有完整的 **v6.9.0**。
- **marvin-ppt** 是 Marvin 的制稿与分层复刻规则，调用本机的 ppt-master。 [查看个人 Skill](skills/marvin-ppt/SKILL.md)

## 一次安装

在目标电脑的 Codex 里输入下面这句话：

> 用 geekmarvin/marvin-ppt 仓库的双 Skill 安装包，在这台电脑一次装好 ppt-master 和 marvin-ppt，并按仓库说明准备运行依赖。

Codex 可以用 Git 下载本仓库，再运行仓库根目录的 `python install.py`。手动下载时，点击仓库的 **Code → Download ZIP**，解压后运行同一个安装程序。安装程序会校验附带的官方原包，安装两个 Skill，并保留目标电脑上已有的同名 Skill。自定义过 Codex 技能目录时，可用 `--dest` 指定实际的 `skills` 目录。 [安装程序](install.py)

使用 PPT Master 需要 Python。Codex 可用同一个 Python 根据安装程序给出的 `requirements.txt` 路径准备依赖。图片复刻如需补绘，还需可用的参考图编辑能力。

安装后新开一个 Codex 对话，用 `$marvin-ppt` 开始制作。

## 使用示例

> 用 $marvin-ppt 把这张 16:9 参考图复刻成可编辑 PowerPoint。补完整被盖住的底图，把需要单独改换的文字、形状和图片拆开。

> 用 $marvin-ppt 把这份定稿文案做成可编辑 PPT，保留文案和页序。

## 版本与许可

仓库的 `vendor` 目录附带 [Hugo He 的官方 PPT Master v6.9.0 发布包](https://github.com/hugohe3/ppt-master/releases/tag/v6.9.0)。其 MIT 许可、作者署名和第三方素材说明均随官方原包保留。两个 Skill 分开安装，以后可单独更新 `ppt-master`，个人规则仍在 `marvin-ppt` 目录。 [上游更新说明](https://github.com/hugohe3/ppt-master#updating-later)
