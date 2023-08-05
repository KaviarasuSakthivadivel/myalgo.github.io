Description

scaling computing system checks its average utilization every second while it monitors. It implements an autoscale policy to increase or reduce instances depending on the current load as described below.

Once an action of increasing or reducing the number of instances is performed, the system will stop monitoring for 10 seconds.

During that time, the number of instances does not change.

- If the average utilization < 25%, then an action is instantiated to reduce the number of instances by half if the number of instances is greater than 1. Take the ceiling if the number is not an integer. If the number of instances is 1, take no action.
- If 25% s average utilization s 60%, take no

action.

If the average utilization > 60%, then an action is instantiated to double the number of instances if the doubled value does not exceed 2 * 10% If the number of instances exceeds this limit upon doubling, take no

action.

Given an array of integers that represent the average utilization at each second, determine the number of instances at the end of the time frame

```java
public static int finalInstances (int instances, List<Integer> averageUtil) {
        int n = averageUtil.size(), i = 0;
        while (i < n) {
            if (averageUtil.get(i) < 25) { // scale down the instances
                instances = Math.max(1, (int) Math.ceil(instances / 2f));
                if (instances > 1) {
                    i += 11;
                } else {
                    i++;
                }
            } else if (averageUtil.get(i) >= 25 && 60 >= averageUtil.get(i)) { // No action
                i++;
            } else if (averageUtil.get(i) > 60) { // Scale up
                double newInstances = (double) instances * 2;
                if (newInstances < 2 * Math.pow(10, 8)) {
                    instances = (instances * 2);
                    i += 11;
                } else {
                    i++;
                }
            }
        }
        return instances;
    }
```