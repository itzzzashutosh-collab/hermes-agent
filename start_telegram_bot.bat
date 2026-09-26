@echo off
title Swatch Paints - Hermes Telegram & WhatsApp Gateway
color 0A
echo =====================================================================
echo          SHARMA INDUSTRIES / SWATCH PAINTS EXECUTIVE GATEWAY
echo =====================================================================
echo Starting Hermes Multi-Platform Gateway (Telegram + WhatsApp)...
echo.

cd /d "d:\Sharma Industries Erp Software\hermes-agent"
".venv\Scripts\python.exe" -m hermes_cli.main gateway run

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Gateway exited with error code %ERRORLEVEL%.
    pause
)
