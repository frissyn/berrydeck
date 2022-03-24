static const int OFN_FILEMUSTEXIST = 0x1000;
static const int OFN_NOCHANGEDIR   = 8;
static const int OFN_PATHMUSTEXIST = 0x800;

typedef bool BOOL;
typedef char CHAR;

typedef unsigned short WORD; 
typedef unsigned long DWORD;

typedef void *PVOID;
typedef void *LPVOID;
typedef void *LPOFNHOOKPROC;

typedef unsigned long HANDLE;
typedef HANDLE HWND;
typedef HANDLE HINSTANCE;

typedef const char *LPCSTR;
typedef const char *LPCTSTR;

typedef char *LPSTR;
typedef char *LPTSTR;

typedef unsigned long LPARAM;

typedef struct {
    DWORD         lStructSize;
    HWND          hwndOwner;
    HINSTANCE     hInstance;
    LPCTSTR       lpstrFilter;
    LPTSTR        lpstrCustomFilter;
    DWORD         nMaxCustFilter;
    DWORD         nFilterIndex;
    LPTSTR        lpstrFile;
    DWORD         nMaxFile;
    LPTSTR        lpstrFileTitle;
    DWORD         nMaxFileTitle;
    LPCTSTR       lpstrInitialDir;
    LPCTSTR       lpstrTitle;
    DWORD         flags;
    WORD          nFileOffset;
    WORD          nFileExtension;
    LPCTSTR       lpstrDefExt;
    LPARAM        lCustData;
    LPOFNHOOKPROC lpfnHook;
    LPCTSTR       lpTemplateName;
    
    LPVOID        pvReserved;
    DWORD         dwReserved;
    DWORD         flagsEx;

} OPENFILENAME;

BOOL GetSaveFileNameA( OPENFILENAME lpofn );
BOOL GetOpenFileNameA( OPENFILENAME *lpofn );

DWORD GetLastError(void);