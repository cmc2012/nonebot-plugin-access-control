nonebot-plugin-access-control for OneBot V11
========

## 主体定义

从上往下优先级从高到低

| 主体                         | 含义           | 示例                       | 必定存在             |
|----------------------------|--------------|--------------------------|------------------|
| qq:<user_id>               | 用户           | qq:12345678              | 是                |
| onebot:<user_id>           | 用户（与上一条含义相同） | onebot:12345678          | 是                |
| superuser                  | 超级用户         |                          | 仅当该用户为超级用户时存在    |
| qq:g<group_id>             | 群组           | qq:g87654321             | 仅当消息来自群组或临时会话时存在 |
| onebot:g<group_id>         | 群组（与上一条含义相同） | onebot:g87654321         | 仅当消息来自群组或临时会话时存在 |
| qq:g<group_id>.group_owner | 群主           | qq.g87654321.group_owner | 仅当消息来自群组或临时会话时存在 |
| qq:group_owner             | 群主           |                          | 仅当消息来自群组或临时会话时存在 |
| qq:g<group_id>.group_admin | 群管理          | qq.g87654321.group_admin | 仅当消息来自群组或临时会话时存在 |
| qq:group_admin             | 群管理          |                          | 仅当消息来自群组或临时会话时存在 |
| qq                         | QQ用户         |                          | 是                |
| onebot                     | OneBot用户     |                          | 是                |
| all                        | 所有用户         |                          | 是                |