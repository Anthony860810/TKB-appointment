# TKB自動預約程式
## 實作
下面為兩種方式來達到目的
1. 第一種維用selenium來自動化控制滑鼠達成目的，但由於仍會因為受到封包傳送時間延誤導致錯過時間，進而延伸出另一種方法
2. 第二種方式為預先處理好所有的封包並於預設時間開始發送封包，直到server接受並回傳成功才停止
