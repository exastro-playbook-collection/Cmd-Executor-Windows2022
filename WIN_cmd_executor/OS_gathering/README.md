Ansible Role: WIN_cmd_executor/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2022に関する任意の設定コマンド実行、任意パスにファイルのアップロード、指定したファイルおよびディレクトリのダウンロードを行います。

# Supports
- 管理マシン(Ansibleサーバ)
  * Linux系OS（AlmaLinux8.10）
  * Ansible バージョン 2.18.0 以上 (動作確認バージョン [core 2.18.1])
  * Python バージョン 3.12以上  (動作確認バージョン 3.12.1)
- 管理対象マシン
  * Windows Server 2022

# Requirements
- 管理マシン(Ansibleサーバ)
  * Ansibleサーバは管理対象マシンへPowershell接続できる必要があります。
- 管理対象マシン
  * Windows Server 2022
  * Powershell3.0+

# Dependencies

本ロールでは、以下のロール、共通部品を利用しています。

- gathering ロール
- パラメータ生成共通部品(parameter_generate)

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に必ず指定しなければならない変数値はありません。

## Optional Variables

ロール利用時に以下の変数値を指定することができます。

| Name | Default Value | Description |
| ---- | ------------- | ----------- |
| `VAR_OS_gathering_dest` | '{{ playbook_dir }}/_gathered_data' | 収集した設定情報の格納先パス。 |
| `VAR_OS_extracting_dest` | '{{ playbook_dir }}/_parameters' | 生成したパラメータの出力先パス。 |
| `VAR_OS_python_cmd` | 'python3' | Ansible実行マシン上で、パラメータファイル作成時に使用するpythonのコマンド。 |
| `VAR_OS_gathering_result` | VAR_WIN_cmd_executor | yaml形式で出力された収集結果登録用ファイル中の収集対象の変数名。<br>「VAR_WIN_cmd_executor」を固定 |
| `VAR_WIN_CommandExecutor_gather` |  |  |
| `- type` | - | 以下のいずれかのタイプを指定する。<br/>command：win_commandでコマンドを実行。コマンドを安全に使用する場合に最適。<br/>shell：win_shellでコマンドを実行。シェルを使用し、リダイレクト、コマンドチェーン等使用可能で高い利便性。<br/>file：指定したファイルをダウンロード。<br/>directory：指定したディレクトリをダウンロード。 |
| &nbsp;&nbsp;&nbsp;&nbsp;`cmd` | - | 実行したいコマンドを指定する。<br/>typeがcommandとshellの場合に有効。<br/>例：Get-WindowsUpdate -Install -AcceptEula |
| &nbsp;&nbsp;&nbsp;&nbsp;`chdir` | - | 移動先のディレクトリパスを指定する。<br/>typeがcommandとshellの場合に有効。<br/>指定したディレクトリに移動してからcmdに指定したコマンドが実行される。<br/>例：C:\\somedir |
| &nbsp;&nbsp;&nbsp;&nbsp;`executable` | - | コマンドを実行するときに使われるシェルを指定する。<br/>typeがshellの場合に有効。ディフォルトはpowershell。<br/>例１：powershell<br/>例２：cmd |
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | - | ダウンロード対象ファイルまたはディレクトリのパス。<br/>typeがfileとdirectoryの場合に有効。<br/>例：C:\\Temp\\renamed-foo.conf<br/>        C:\Temp |

# Results

本ロールの出力について説明します。

## 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_cmd_executor/`

本ロールを既定値で利用した場合、以下のように設定情報を格納します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _gathered_data/
         └── 管理対象マシンホスト名 or IPアドレス/
              └── OS/  # OS設定ロール向け専用のフォルダ
                   └── パラメータ生成対象/  # 収集データ
                        └── 代入順序/
                             └── customize/
                                  ・・・
~~~

## 生成したパラメータの出力例

生成したパラメータは以下のディレクトリ・ファイル名で出力します。

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_cmd_executor.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_cmd_executor.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description |
| ---- | ----------- |
| `VAR_WIN_cmd_executor` |     |
| `- type` | 収集の時に、指定したタイプ。<br/>command：win_commandでコマンドを実行。コマンドを安全に使用する場合に最適。<br/>shell：win_shellでコマンドを実行。シェルを使用し、環境変数、パイプ・リダイレクト等使用可能で高い利便性。<br/>file：指定したファイルをダウンロード。<br/>directory：指定したディレクトリをダウンロード。 |
| &nbsp;&nbsp;&nbsp;&nbsp;`cmd` | 収集の時に、指定したコマンド。typeがcommandとshellの場合に有効。 |
| &nbsp;&nbsp;&nbsp;&nbsp;`chdir` | 収集の時に、指定した移動先のディレクトリパス。typeがcommandとshellの場合に有効。 |
| &nbsp;&nbsp;&nbsp;&nbsp;`executable` | 収集の時に、指定したコマンドを実行するときに使われるシェル。typeがshellの場合に有効。 |
| &nbsp;&nbsp;&nbsp;&nbsp;`stdout` | コマンド標準出力(stdout)のログファイル。typeがcommandとshellの場合に有効。 |
| &nbsp;&nbsp;&nbsp;&nbsp;`stderr` | コマンド標準エラー出力(stderr)のログファイル。typeがcommandとshellの場合に有効。 |
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | 収集の時に、指定したダウンロード対象ファイルまたはディレクトリのパス。typeがfileとdirectoryの場合に有効。 |
| &nbsp;&nbsp;&nbsp;&nbsp;`file` | typeがfileの場合、ダウンロード対象ファイル。<br/>typeがdirectoryの場合、ダウンロード対象ディレクトリの圧縮ファイル。 |
| &nbsp;&nbsp;&nbsp;&nbsp;`dircontent` | ダウンロード対象ディレクトリの階層を記録したファイル。typeがdirectoryの場合に有効。 |

### Example
~~~
---
VAR_WIN_cmd_executor:
- cmd: Get-NetIPAddress -AddressFamily IPv4
  stderr: /0/customize/0/stderr.txt
  stdout: /0/customize/0/stdout.txt
  type: shell
- cmd: Get-NetIPAddress -AddressFamily IP
  stderr: /1/customize/0/stderr.txt
  stdout: /1/customize/0/stdout.txt
  type: shell
- file: /2/customize/0/C:/download/test.cgi
  path: C:\download\test.cgi
  type: file
- file: /3/customize/0/C:/upload/test.cgi
  path: C:\upload\test.cgi
  type: file
・・・
~~~

# Usage

本ロールの利用例について説明します。

## 既定値で設定情報収集およびパラメータ生成を行う場合

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── WIN_cmd_executor/
    │         └── OS_gathering/
    │              │── defaults/
    │              │      main.yml
    │              │── files/
    │              │      extracting.py
    │              │── tasks/
    │              │      check.yml
    │              │      check_parameter.yml    
    │              │      gathering.yml
    │              │      gathering_definition_set_fact.yml    
    │              │      generate.yml
    │              │      main.yml
    │              │── vars/
    │              │      gathering_definition.yml
    │              │      gathering_definition_task_command.yml
    │              │      gathering_definition_task_file.yml
    │              │      gathering_definition_task_shell.yml
    │              └─ README.md
    └─ master_playbook.yml
~~~

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: WIN_cmd_executor/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_cmd_executor/  # 収集データ
    │                    └── 代入順序/
    │                        └── customize/
    │                     　　　　　．．．
    │                    └── 代入順序/
    │                        └── customize/
    │                             ．．．
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_cmd_executor.yml  # パラメータ
~~~

## パラメータ再利用

以下の例では、生成したパラメータを使用してOSの設定を変更します。

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: WIN_cmd_executor/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_cmd_executor.yml  # パラメータ
~~~

- 生成したパラメータを指定してplaybookを実行

~~~
> ansible-playbook master_playbook.yml -i hosts
~~~

# Remarks
-------

# License
-------

# Copyright
---------
Copyright (c) 2025 NEC Corporation

# Author Information
------------------
NEC Corporation
