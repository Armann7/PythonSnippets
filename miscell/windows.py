import subprocess

import win32ts
import pywintypes
import win32con
import win32security


def popen():
    with subprocess.Popen(["query.exe", "session"], stdout=subprocess.PIPE, encoding="utf-8", shell=True, text=True) as proc:
        print(proc.stdout.read())


def list_sessions():
    """ Finds any disconnected terminal service sessions and logs them off"""
    sessions = win32ts.WTSEnumerateSessions(win32ts.WTS_CURRENT_SERVER_HANDLE)
    for session in sessions:
        """
        WTS_CONNECTSTATE_CLASS: WTSActive,WTSConnected,WTSConnectQuery,WTSShadow,WTSDisconnected,
              WTSIdle,WTSListen,WTSReset,WTSDown,WTSInit
        """
        print(session)
        sessionid = session['SessionId']
        username = win32ts.WTSQuerySessionInformation(win32ts.WTS_CURRENT_SERVER_HANDLE, sessionid, win32ts.WTSUserName)
        print(username)


def logon_user():
    try:
        handle = win32security.LogonUser("robot", "", "chappy", win32con.LOGON32_LOGON_INTERACTIVE, win32con.LOGON32_PROVIDER_DEFAULT)
    except pywintypes.error as err:
        print(f"Failed to login. Error: {err}")
    else:
        print("Successful to login")
        handle.Close()


if __name__ == "__main__":
    # popen()
    list_sessions()
    logon_user()
