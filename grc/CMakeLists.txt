
########################################################################
# Install GRC xml files
########################################################################

list(APPEND grc_sources
    phase-comparator.xml
)

install(
    FILES ${grc_sources}
    DESTINATION ${GRC_BLOCKS_DIR}
    COMPONENT "grphasecomparator_python"
)
