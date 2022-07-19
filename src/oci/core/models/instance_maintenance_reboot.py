# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceMaintenanceReboot(object):
    """
    The maximum possible date and time that a maintenance reboot can be extended.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceMaintenanceReboot object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_maintenance_reboot_due_max:
            The value to assign to the time_maintenance_reboot_due_max property of this InstanceMaintenanceReboot.
        :type time_maintenance_reboot_due_max: datetime

        """
        self.swagger_types = {
            'time_maintenance_reboot_due_max': 'datetime'
        }

        self.attribute_map = {
            'time_maintenance_reboot_due_max': 'timeMaintenanceRebootDueMax'
        }

        self._time_maintenance_reboot_due_max = None

    @property
    def time_maintenance_reboot_due_max(self):
        """
        **[Required]** Gets the time_maintenance_reboot_due_max of this InstanceMaintenanceReboot.
        The maximum extension date and time for the maintenance reboot, in the format defined by
        `RFC3339`__.
        The range for the maintenance extension is between 1 and 14 days from the initial scheduled maintenance date.
        Example: `2018-05-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_maintenance_reboot_due_max of this InstanceMaintenanceReboot.
        :rtype: datetime
        """
        return self._time_maintenance_reboot_due_max

    @time_maintenance_reboot_due_max.setter
    def time_maintenance_reboot_due_max(self, time_maintenance_reboot_due_max):
        """
        Sets the time_maintenance_reboot_due_max of this InstanceMaintenanceReboot.
        The maximum extension date and time for the maintenance reboot, in the format defined by
        `RFC3339`__.
        The range for the maintenance extension is between 1 and 14 days from the initial scheduled maintenance date.
        Example: `2018-05-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_maintenance_reboot_due_max: The time_maintenance_reboot_due_max of this InstanceMaintenanceReboot.
        :type: datetime
        """
        self._time_maintenance_reboot_due_max = time_maintenance_reboot_due_max

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
