# holoeml-amp

> **Windows only.** The Thorlabs TSI SDK and its native DLLs are Windows-specific. This project does not support Linux or macOS.

## Setup

### 1. Install dependencies

```powershell
uv sync
```

### 2. Thorlabs TSI Camera SDK

`thorlabs_tsi_sdk` is not on PyPI. It ships with the **ThorCam** desktop application.

**Step 1 — Download and install ThorCam**

Download ThorCam from the [Thorlabs Scientific Imaging software page](https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=ThorCam) and run the installer.

**Step 2 — Locate the SDK**

After installation the SDK is typically found at:

```
C:\Program Files\Thorlabs\Scientific Imaging\ThorCam\
```

Look for a folder called **Scientific Camera Interfaces** or similar, containing a `Python Toolkit` subfolder.

**Step 3 — Copy the SDK into the project**

Copy the entire SDK folder into the project root as `thorcam-sdk/`:

```
thorcam-sdk/
  Python Toolkit/
    thorlabs_tsi_camera_python_sdk_package.zip
    dlls/
    ...
  Native Toolkit/
    dlls/
    ...
```

**Step 4 — Install the Python package**

```powershell
uv add "thorcam-sdk/Python Toolkit/thorlabs_tsi_camera_python_sdk_package.zip"
```

**Step 5 — DLL visibility**

The native DLLs must be on the PATH at runtime. `src/pythorcam/windows_setup.py` handles this automatically — call `configure_path()` before importing the SDK:

```python
from pythorcam.windows_setup import configure_path
configure_path()
from thorlabs_tsi_sdk.tl_camera import TLCameraSDK
```
