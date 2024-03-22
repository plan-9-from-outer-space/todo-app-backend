@echo off

@REM curl -X POST ^
@REM      "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:countTokens?key=%API_KEY%" ^
@REM      -H "Content-Type: application/json" ^
@REM      -d "{ \"contents\": [{ \"parts\": [{ \"text\": \"Write a story about a magic backpack.\" }]}]}" ^
@REM      > response.json

@REM curl -X GET ^
@REM   "http://127.0.0.1:8000/?token=jessica" ^
@REM   -H "accept: application/json" ^
@REM   -H "x-token: fake-super-secret-token"

@REM curl -X GET ^
@REM   "http://127.0.0.1:8000/items" ^
@REM   -H "accept: application/json" ^
@REM   -H "x-token: fake-super-secret-token" ^
@REM   -H "x-key: fake-super-secret-key" ^
@REM   -L

@REM 1 for Standard Output and 2 for Standard Error
@REM curl -X GET "http://127.0.0.1:8000" 1> output.json 2>NUL
@REM

curl -X GET "http://127.0.0.1:8000"

echo.
