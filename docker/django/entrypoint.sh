#!/bin/sh

set -e

(
    set -x
)

restart_error_handler() {
    echo "Restart ${0} in 3 sec..."
    sleep 3
    (
        set -x
        exec ${0} reload
    )
}
trap restart_error_handler 0

echo "_______________________________________________________________________"
echo "$(date +%c) - ${0} $*"

(
    set -x
    python ./manage.py collectstatic --no-input
    python ./manage.py migrate
    granian --interface wsgi core.wsgi:application --host 0.0.0.0 --port 8000 --workers=6
    echo "runserver terminated with exit code: $?"
    sleep 3
    exit 1
)

exit 2