@ECHO OFF
Write-Output 'Custom PowerShell profile in effect!'
Add-Content -Path 'D:\praxis-academy\MyScript.ps1' -Value "[ZoneTransfer]`nZoneId=3" -Stream 'Zone.Identifier'
Clear-Content -Path 'D:\praxis-academy\MyScript.ps1' -Stream 'Zone.Identifier'
PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%~dpn0.ps1'"
Pause