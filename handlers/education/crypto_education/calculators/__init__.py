from .menu import (
    crypto_calculators_menu,
    crypto_calculators_router,
)

# =========================
# BTC
# =========================

from .btc_converter import (
    btc_converter_handler,
)

# =========================
# ETH
# =========================

from .eth_converter import (
    eth_converter_intro,
    ethereum_input,
)

# =========================
# Satoshi
# =========================

from .satoshi import (
    satoshi_converter_intro,
    satoshi_input,
)

# =========================
# DCA
# =========================

from .dca import (
    dca_start,
    dca_capital,
    dca_count,
    dca_interval,
)

# =========================
# Staking
# =========================

from .staking import (
    staking_intro,
    staking_input,
)

# =========================
# Profit / Loss
# =========================

from .profit_loss import (
    profit_loss_handler,
)

# =========================
# Drawdown
# =========================

from .drawdown import (
    drawdown_handler,
)

__all__ = [

    "crypto_calculators_menu",
    "crypto_calculators_router",

    # BTC
    "btc_converter_handler",

    # ETH
    "eth_converter_intro",
    "ethereum_input",

    # SATOSHI
    "satoshi_converter_intro",
    "satoshi_input",

    # DCA
    "dca_start",
    "dca_capital",
    "dca_count",
    "dca_interval",

    # STAKING
    "staking_intro",
    "staking_input",

    # PROFIT / LOSS
    "profit_loss_handler",

    # DRAWDOWN
    "drawdown_handler",
]