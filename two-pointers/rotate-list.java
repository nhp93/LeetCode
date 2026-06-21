/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) {
            return null;
        }
        int count = 0;
        ListNode curr = head;
        ListNode tail = head;
        while (curr != null) {
            count++;
            tail = curr;
            curr = curr.next;
        }
        tail.next = head;
        curr = head;
        int rot = k % count;
        ListNode newTail = head;
        for (int i = 0; i < count - rot - 1; i++ ) {
            newTail = newTail.next;
        }
        head = newTail.next;
        newTail.next = null;
        return head;
    }
}