from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" CHAR(36) NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(50) NOT NULL,
    "last_name" VARCHAR(50) NOT NULL,
    "email" VARCHAR(100) NOT NULL UNIQUE,
    "password" VARCHAR(150) NOT NULL,
    "is_admin" INT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP,
    "is_deleted" INT NOT NULL DEFAULT 0,
    "permission_groups" JSON
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztl21P2zAQx79KlVdMYoiWlqFpmtRCJzpROkG7TSAUubGbWjh2sJ1Bhfju87lJ89Cmay"
    "sY68QbRP53V9/9fH56dAKBCVN7A0Wk87Hy6HAUEPNPTt+tOCgMUxUEjYbMOkbGwypoqLRE"
    "njbiCDFFjISJ8iQNNRXcqDxiDEThGUfK/VSKOL2LiKuFT/TYJnJ9Y2TKMXkgKvkMb90RJQ"
    "zn8qQYxra6qyeh1QaDzskX6wnDDV1PsCjgqXc40WPBZ+5RRPEexIDNJ5xIpAnOlAFZxuUm"
    "0jRjI2gZkVmqOBUwGaGIAQzn0yjiHjCo2JHgT/2zswYeT3BAS7kGFo9P06rSmq3qwFDHp8"
    "2LnYPDd7ZKobQvrdEScZ5sINJoGmq5piBHVCrt2q85oMdjJBcDzUcVwJqkN0GaCCnTtJ8S"
    "qAmszQg6AXpwGeG+HpvPxv4Sot+bFxZqY99CFabDp31/Hltq1gRsU5YMbYAyF/RGckqSBI"
    "iydSjOAp6H4J+X93Pyq+6vAtB4lRK0tjzCECl1L+SCfbKcYjZmO1uxulIvVpc0Y3W+G6ly"
    "EQ4on0fZEoIRxEtOnUxYgebQxL0UznVP4dWPmVavdwZZB0rdMSt0+gWMg26rbfhausaJai"
    "t3zvsFpJ4kULaL9DzUE2PRNCCLqeYjC1xxHLqX/LMC5Hhp/82WNSXgHmeTePQlyPudbvuy"
    "3+x+y3E/afbbYKlZdVJQdw4LzT37kcqPTv+0Ap+Vq955u3hdmPn1rxzICUVauFzcmzbO7I"
    "GJmoDJzWsU4g3nNR+5lfO6JfOYlL10Is3mZe78BOiuvetlAt/2vcKpTGRAlTK5ub4UUajm"
    "6X697J2XHM+LgguEB9yYrzH19G6FUaVvtm2lQPk52MnRvNNt/iye2sdnvVax++EHWgY7vB"
    "1Ht5lHDwhD5N3eI4ndOYuoiTLfeVNQC4oK4si3rKBiqC9+SjeJpN7YWfDIji27y57ZKPX5"
    "Z97ZHa7XeGabKS+2YNxvr3oB92GU97Vq/UP96OCwfmRcbCYz5cOSHk3Wdfmz+heRsE7XuX"
    "xnQrbz7l1rNFa4exuv0ru3teU3TFgaa0CM3bcT4Iu8A82ImvAF17HycyYT8gynyytg/e+P"
    "l6ffLEfz6g=="
)
