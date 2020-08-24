#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from tobrot.get_cfg import get_config


class Commandi:
    LEECH = get_config(
        "COMMANDI_LEECH",
        "leech@VC_torrentbot"
    )
    PURGE = get_config(
        "COMMANDI_PURGE",
        "purge@VC_torrentbot"
    )
    YTDL = get_config(
        "COMMANDI_YTDL",
        "ytdl@VC_torrentbot"
    )
    STATUS = get_config(
        "COMMANDI_STATUS",
        "status@VC_torrentbot"
    )
    CANCEL = get_config(
        "COMMANDI_CANCEL",
        "cancel"
    )
    EXEC = get_config(
        "COMMANDI_EXEC",
        "exec@VC_torrentbot"
    )
    EVAL = get_config(
        "COMMANDI_EVAL",
        "eval@VC_torrentbot"
    )
    RENAME = get_config(
        "COMMANDI_RENAME",
        "rename@VC_torrentbot"
    )
    UPLOAD = get_config(
        "COMMANDI_UPLOAD",
        "upload@VC_torrentbot"
    )
    HELP = get_config(
        "COMMANDI_HELP",
        "help@VC_torrentbot"
    )
    SAVETHUMBNAIL = get_config(
        "COMMANDI_SAVETHUMBNAIL",
        "savethumbnail@VC_torrentbot"
    )
    CLEARTHUMBNAIL = get_config(
        "COMMANDI_CLEARTHUMBNAIL",
        "clearthumbnail@VC_torrentbot"
    )
    GET_RCLONE_CONF_URI = get_config(
        "COMMANDI_GET_RCLONE_CONF_URI",
        "getrcloneconfuri@VC_torrentbot"
    )
    UPLOAD_LOG_FILE = get_config(
        "COMMANDI_UPLOAD_LOG_FILE",
        "log@VC_torrentbot"
    )
