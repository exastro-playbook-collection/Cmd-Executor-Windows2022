Cmd-Executor-Windows2022
===============================
# Trademarks
-----------
* Linuxは、Linus Torvalds氏の米国およびその他の国における登録商標または商標です。
* RedHat、RHEL、CentOSは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
* Windows、PowerShell、IIS、.NET Frameworkは、Microsoft Corporation の米国およびその他の国における登録商標または商標です。
* Ansibleは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
* pythonは、Python Software Foundationの登録商標または商標です。
* NECは、日本電気株式会社の登録商標または商標です。
* その他、本ロールのコード、ファイルに記載されている会社名および製品名は、各社の登録商標または商標です。

# Description
-----------
Windows Server 2022に関する任意の設定コマンド実行、および任意パスにファイルのアップロードを行うロールを提供します。

-------------

## 注意
OS関連のロール利用は、パラメータ内容を十分に確認し、事前評価を行ってからご利用ください。パラメータ値が誤っていると、ターゲットマシンへのアクセスができなくなるなど、トラブルが発生する可能性があります。

-------------

# Specification

## Ansibleサーバ

* Ansible バージョン 2.11.0 以上 (動作確認バージョン [core 2.11.12])
* Python バージョン 3.x  (動作確認バージョン 3.6.8、3.9.18)

# OS用ロールを使うまでの前準備
OS用ロールを利用する前に、ターゲットマシン(管理対象サーバ)へ事前に実施してください。

## ターゲットマシンの条件
* PowerShell のバージョンが3以上であること
* WinRM での接続が許可されていること
* PowerShell のリモート実行が許可されていること
* 管理者グループに属したAnsibleからの接続用ユーザーがあること

## WinRM の接続設定
Ansible-PJが公式に提供しているセットアップスクリプトでWinRMの接続設定を行います。

1. PowerShell を管理者権限で起動してください。
   * スタートメニューで[Windows PowerShell]アイコンを右クリックして「管理者として実行」でPowerShell を起動してください。
2. セットアップスクリプトのダウンロード
   * 以下のコマンドラインで、`ConfigureRemotingForAnsible.ps1` を入手します。

~~~
 PS C:\tmp> Invoke-WebRequest -Uri https://raw.githubusercontent.com/ansible/ansible-documentation/devel/examples/scripts/ConfigureRemotingForAnsible.ps1 -OutFile ConfigureRemotingForAnsible.ps1
~~~

3. セットアップスクリプトを実行

~~~
 PS C:\tmp> powershell -ExecutionPolicy RemoteSigned .\ConfigureRemotingForAnsible.ps1
~~~


# 提供ロール一覧
## 情報設定ロール一覧
情報の設定に使用する以下のロールを提供します。

| ロール名                            | Description                      |
| ----------------------------------- | -------------------------------- |
| [WIN_cmd_executor/OS_build](WIN_cmd_executor/OS_build) | 任意の設定コマンド実行、および任意パスにファイルのアップロード |

## 情報設定ロールのマニュアル一覧
各ロールで情報設定可能なパラメータは、以下の各ロールのマニュアル内のRole Variablesセクションに記載されたものとなります。

| 情報設定ロールのマニュアル |
| ------- |
| [WIN_cmd_executor/OS_build マニュアル](WIN_cmd_executor/OS_build/README.md) |

# Remarks
-------
OS仕様に依存する情報の設定ロールでは、実行は成功するが設定したパラメタが反映されない場合があります。<br>
各ロールの変数説明に該当する内容は、OSエディションによって、内容が変わる場合があります。<br>

# License
-------

# Copyright
---------
Copyright (c) 2025 NEC Corporation

# Author Information
------------------
NEC Corporation
