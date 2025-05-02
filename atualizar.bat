@echo off
cd /d C:\Users\lucas\OneDrive\Documentos\gestor-pecas-pro
git add .
git commit -m "Atualização automática em %date% %time%"
git push origin main
pause
