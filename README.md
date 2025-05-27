# MyDocs

个人自用，一些自己存放用于保存在云端的零碎文档，开源用以参考借鉴。

---
utils.sh
一些自己写的sh脚本，感兴趣者可以自己复制到 .bashrc 或别的配置中。或者下载该文件后，直接在 .bashrc 中添加：
```sh
source "/[[该文件的目录]]/utils.sh"
```

需要者也可以重新命名这些命令。

- `gccfast`: 快速编译并运行 C/C++ 文件，默认输出 a.out
    - `<source_file>`: 源文件路径。
    - `[compiler_flags]`: 传递给编译器的额外选项。例如 -O2, -g, -lm等。
    - `--`: 一个可选的分隔符。它之后的任何参数都将作为程序的运行时参数传递给编译生成的可执行文件 (./a.out)。
    - `[program_arguments]`: 传递给最终执行程序的参数。
- `lsgit`: ls 但是会按照.gitignore的规则过滤
    - `-l`: 启用详细列表模式
    - `[ls_options]`: 当使用 `-l` 时，其后的所有选项都将传递给 `ls` 命令。（例如`-h`, `-a`）
- `treegit`: tree 但是会按照.gitignore的规则过滤，所有 `tree` 命令支持的选项都可以直接传递给 `treegit`。
    - `-L <level>`: 限制显示深度。例如 `treegit -L 2`。
    - `-a`: 显示所有文件（包括隐藏文件，但仍遵守 `.gitignore` 规则）。
    - `-d`: 只显示目录。
    - `-F`: 在目录名后添加类型指示符（`/` 表示目录，`*` 表示可执行文件等）。
    - `-h`: 以人类可读的格式显示文件大小。

---

6 steps to a successful research pr.txt
写PR的经验，忘记从哪里下载的了，感觉言简意赅很好用。

---

`Paradox Interactive/`
`My Games/`
这些是本人制作的多个游戏mod的版本控制。
对相关游戏的 mod 制作感兴趣者可以参考学习。

---

Other
...

