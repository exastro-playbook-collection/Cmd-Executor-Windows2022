Ansible Role: WIN_cmd_executor/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関する任意の設定コマンド実行、および任意パスにファイルのアップロードを行います。

# Supports
- 管理マシン(Ansibleサーバ)
  * Linux系OS（RHEL8）
  * Ansible バージョン 2.11.0 以上 (動作確認バージョン [core 2.11.12])
  * Python バージョン 3.x  (動作確認バージョン 3.6.8、3.9.18)
- 管理対象マシン
  * Windows Server 2022

# Requirements
- 管理マシン(Ansibleサーバ)
  * Ansibleサーバは管理対象マシンへPowershell接続できる必要があります。
- 管理対象マシン
  * Windows Server 2022
  * Powershell3.0+

# Dependencies

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。<br>
<br>
「値変更可能列」について<br>
  ◎：キーのため変更不可の変数（更新、削除の場合）<br>
  〇：値が変更できる変数<br>

| Name     | 値変更可能 | Description |
| -------- | :-----------: | ----------- |
| `VAR_WIN_CommandExecutor` |||
| &nbsp;&nbsp;&nbsp;&nbsp;`type` |     〇     | 以下のいずれかのタイプを指定する。<br>command：win_commandでコマンドを実行。コマンドを安全に使用する場合に最適。<br>shell：win_shellでコマンドを実行。シェルを使用し、リダイレクト、コマンドチェーン等使用可能で高い利便性。<br>upload：ファイルをアップロードして指定のパスに配置する。 |
| &nbsp;&nbsp;&nbsp;&nbsp;`cmd` | 〇 | 実行したいコマンドを指定する。<br>typeがcommandとshellの場合に有効。<br>例：Get-WindowsUpdate -Install -AcceptEula |
| &nbsp;&nbsp;&nbsp;&nbsp;`chdir` | 〇 | 移動先のディレクトリパスを指定する。<br>typeがcommandとshellの場合に有効。<br>指定したディレクトリに移動してからcmdに指定したコマンドが実行される。<br>例：C:\\somedir |
| &nbsp;&nbsp;&nbsp;`executable` | 〇 | コマンドを実行するときに使われるシェルを指定する。<br>typeがshellの場合に有効。ディフォルトはpowershell。<br>例１：powershell<br>例２：cmd |
| &nbsp;&nbsp;&nbsp;`path` | 〇 | アップロードするファイルの配置先パスを指定する。<br>typeがuploadの場合に有効。<br>例：C:\\Temp\\renamed-foo.conf |
| &nbsp;&nbsp;&nbsp;`file` | 〇 | アップロードするファイルを登録する。<br>typeがuploadの場合に有効。 |

### Example
~~~
VAR_WIN_CommandExecutor:
- type: upload
  path: C:\Temp\somescript.ps1
  file: somescript.ps1
- type: shell
  cmd: somescript.ps1 >> somelog.txt
  chdir: C:\TEMP
~~~

```
- type: shell
  cmd: echo %HOMEDIR%
  executable: cmd
- type: shell
  cmd: Write-Host test
  executable: powershell
```

## Optional Variables

特にありません。

# Usage

特にありません。

# Example Playbook

## ■エビデンスを取得しない場合の呼び出す方法

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── cmd-executor-WS2022
    │          └── OS_build/
    │               │── tasks/
    │               │      build_flat.yml
    │               │      main.yml
    │               └─ README.md
    └─ master_playbook.yml
~~~

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: cmd-executor-WS2022/OS_build
      VAR_WIN_CommandExecutor:
      - type: upload
        path: C:\Temp\somescript.ps1
        file: somescript.ps1
      - type: shell
        cmd: somescript.ps1 >> somelog.txt
        chdir: C:\TEMP
  strategy: free
~~~

- Running Playbook

~~~
> ansible-playbook master_playbook.yml
~~~

## ■Remarks

-------
特にありません。

# License
-------

# Copyright
---------
Copyright (c) 2025 NEC Corporation

# Author Information
------------------
NEC Corporation
