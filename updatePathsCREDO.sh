RELDIR=`dirname $BASH_SOURCE`
export REPOSBASE=`cd $RELDIR; pwd`
export STG_BASEDIR=$REPOSBASE
export CREDO_DIR=$REPOSBASE/credo
export PATH=$CREDO_DIR/scripts/:$PATH
export PYTHONPATH=$CREDO_DIR:$PYTHONPATH
