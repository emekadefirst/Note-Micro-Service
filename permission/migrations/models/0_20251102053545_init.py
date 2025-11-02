from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "permissions" (
    "id" CHAR(36) NOT NULL PRIMARY KEY,
    "action" VARCHAR(6) NOT NULL /* CREATE: create\nREAD: read\nUPDATE: update\nDELETE: delete */,
    "module" VARCHAR(10) NOT NULL /* NOTE: note\nUSER: user\nPERMISSION: permission */,
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP,
    "is_deleted" INT NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "permission_groups" (
    "id" CHAR(36) NOT NULL PRIMARY KEY,
    "title" VARCHAR(55) NOT NULL UNIQUE,
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP,
    "is_deleted" INT NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS "idx_permission__title_672bad" ON "permission_groups" ("title");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS "permission_groups_permissions" (
    "permission_groups_id" CHAR(36) NOT NULL REFERENCES "permission_groups" ("id") ON DELETE CASCADE,
    "permission_id" CHAR(36) NOT NULL REFERENCES "permissions" ("id") ON DELETE CASCADE
);
CREATE UNIQUE INDEX IF NOT EXISTS "uidx_permission__permiss_4949c5" ON "permission_groups_permissions" ("permission_groups_id", "permission_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztWGtv0zwU/itRPoE0pq1sA00IqZe8L0FrO/UCiG2K3MRNoyV2SBygmvbf8XHuV9LSsU"
    "30S1WfS47Pc+zjx76THWpg2z+8xJ5j+b5FiXwu3ckEOZj/qdAeSDJy3VQHAoYWtjB3Ezsh"
    "RwufeUhnXLVEto+5yMC+7lkuCwORwLZBSHVuaBEzFQXE+hZgjVETsxX2uOLqhostYuCf2I"
    "+H7q22tLBt5OZsGRBbyDW2doVsPlcH/wlLCLfQdGoHDkmt3TVbUZKYB4FlHIIP6ExMsIcY"
    "NjJpwCyjpGNROGMuYF6Ak6kaqcDASxTYAIb8bhkQHTCQRCT4OXkvbwCPzhHm0FqEARZ392"
    "FWac5CKkOo/ofu5MXrs5ciS+oz0xNKgYh8LxwRQ6GrwDUFEokplsHsr5CnkMARgKp8Iojo"
    "uARs6l0Al098G1hjQYpruqZiYGPAcijK/YnSnSnnku5hHu+a8OHgXOID45rMLwdCF7iG0A"
    "2UCwXGfGljFib1W/RlB/3UbExMtuLDs4ZifOpORD3CclC+N8J9M4oUHdBAUXI7MLDxtkVI"
    "vR+7CKMxwEoogDyfKhMOuY+9a3KpTIbqdKqOR+eSm2szmwJ/fNQC+eOjWuhBlcc+XDCGhl"
    "gZ/wHXMMvB1V0l71nA3ohcD+M/LSoR9ZA/L0TrniLDBhkTex1FbwB3pg6V6aw7vIREHN//"
    "ZguE+MYCTUdI1wVpaQ8kH5E+q7MPEgylr+ORUmxcid3sqwxzQgGjGqE/NGRkmm0sjYHJ1T"
    "Xc7NvUNe/5LOv6TOoYp91YSMvXwkZdceT3KLUxIjWnfs6xUMcF93yo5rgpD2pfvN54fJGr"
    "W0+dFVrdfNhTeAsUBeNGFhNidTTjfQ/o1PI2wwNAsED67Q/kGVpJQzu0zrascjpOJcGAfq"
    "+ZHg3ccvmGiKxnFH5LJ1yhXCWO+n/8xd0zt51svVSahhBJaLW0O0nJw7ZoQFkIM4x7ST1R"
    "g1u8zmtDmH0tpLtJrcp2oQFbcXNzVf2NQkyuiNgS0JLutN8diM2uZeEXJ4hYC4ggU4gAo/"
    "uD2mQbryEJHm3uItG8H/xGciUzi/HgN/uryUNfTUKgK0lxNZaJw2548EN3ijyzPT1twWxP"
    "T2uZLaj2zHbPbPfM9inUcc9s/w1mm6Vlu6K2T/Gs2p7V1hHazJ2gls/+lsjmCO/O+Wy4Yx"
    "sJbRd7lr6q4rGRppG+otTmybyiq4RtwFRhJRSWa7QsHpVZmRDlVef45M3J29dnJ2+5iZhJ"
    "InnT0IrCjtLETL9jL17abblpxuWRX2m35KedVgS108BQO2WKCltjAxAj8+cJ4PFRu7frps"
    "fr8us1JQyTCiL4cToe1ZD71KUA5JzwBK8MS2cHkm357OZpwtqAImSdYxExeC+G3S9FXPsX"
    "416R1sEHen+VT1QcL/e/AClZn3Q="
)
