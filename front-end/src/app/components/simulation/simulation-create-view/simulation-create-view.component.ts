import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-simulation-create-view',
  templateUrl: './simulation-create-view.component.html',
  styleUrls: ['./simulation-create-view.component.scss']
})
export class SimulationCreateViewComponent implements OnInit {
  appearance: string = 'standard'

  constructor() { }

  ngOnInit(): void {
  }


  factoryConfigForm = new FormGroup({
    requiredItemNames: new FormControl('A, B', [Validators.required, Validators.pattern('[a-zA-Z\\s]+(?:,[a-zA-Z\\s]*)*')]),
    productCode: new FormControl('P', Validators.required),
    emptyCode: new FormControl('E', Validators.required),
    numberOfSimulationSteps: new FormControl('10', [Validators.min(1), Validators.required] ),
    numberOfConveyorBeltSlots: new FormControl('3', [Validators.min(1), Validators.required]),
    numberOfWorkerPairs: new FormControl('3', [Validators.min(1), Validators.required]),
    pickupTime: new FormControl('1', [Validators.min(1), Validators.required]),
    dropTime: new FormControl('1', [Validators.min(1), Validators.required]),
    buildTime: new FormControl('4', [Validators.min(1), Validators.required]),
  })

  onSubmit() {
    console.warn(this.factoryConfigForm.value);
    let requiredItemNames = this.factoryConfigForm.value.requiredItemNames;
    console.log(requiredItemNames);
    requiredItemNames = requiredItemNames.replace(/,/g, ' ');
    console.log(requiredItemNames);
    let requiredItemNamesArray = requiredItemNames.split(' ');

    const output = [];
    for (let item of requiredItemNamesArray) {
      const cleanItem = item.split(' ').join('');
      if (cleanItem !== '') {
        output.push(cleanItem)
      }
    }

    // TODO: before patching the value to show what we really care about we have to call the api and try to post.

    this.factoryConfigForm.patchValue({
      requiredItemNames: output.join(', ')
    })
    console.log(output)
  }

  isControlInvalid(controlName: string): boolean {
    return this.factoryConfigForm.get(controlName).invalid;
  }

  getRequiredItemNamesErrorMessage(): string {
    let message = 'This field is required';
    if (this.factoryConfigForm.get('requiredItemNames').hasError('pattern')) {
      message = 'Only letters, commas and spaces are allowed';
    }

    return message;
  }
}
