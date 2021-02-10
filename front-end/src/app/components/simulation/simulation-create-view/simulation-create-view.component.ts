import {Component} from '@angular/core';
import {FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';
import {SimulationAPIService} from '../../../services/api/simulation/simulation-api.service';
import {NotificationService} from '../../../services/notification/notification.service';

@Component({
  selector: 'app-simulation-create-view',
  templateUrl: './simulation-create-view.component.html',
  styleUrls: ['./simulation-create-view.component.scss']
})
export class SimulationCreateViewComponent {
  appearance = 'standard';

  constructor(
    private fb: FormBuilder,
    private simulationAPIService: SimulationAPIService,
    private notificationService: NotificationService
  ) {}

  simulationForm = this.fb.group({
    name: ['', Validators.required],
    description: [''],
    factoryConfigs: this.fb.array([this.getFactoryConfigFormGroup()]),
  });

  getFactoryConfigFormGroup(): FormGroup {
    return this.fb.group(
      {
        materials: this.fb.array([this.getMaterialControl()]),
        productCode: ['P', Validators.required],
        emptyCode: ['E', Validators.required],
        numberOfSimulationSteps: ['10', [Validators.min(1), Validators.required]],
        numberOfConveyorBeltSlots: ['3', [Validators.min(1), Validators.required]],
        numberOfWorkerPairs: ['3', [Validators.min(1), Validators.required]],
        pickupTime: ['1', [Validators.min(1), Validators.required]],
        dropTime: ['1', [Validators.min(1), Validators.required]],
        buildTime: ['4', [Validators.min(1), Validators.required]],
      }
    );
  }

  getMaterialControl() {
    return this.fb.control(
      'A', [Validators.required, Validators.pattern('([\\w\\-]+)')]
    ) as FormControl;
  }

  addMaterial(factoryConfig) {
    factoryConfig.get('materials').push(this.getMaterialControl());
  }

  deleteMaterial(factoryConfig, materialIndex: number) {
    factoryConfig.get('materials').removeAt(materialIndex);
  }

  getControls(formElement, path: string) {
    return formElement.get(path).controls;
  }

  onSubmit() {
    this.simulationAPIService.create(this.simulationForm.value).subscribe(
      data => {
        this.simulationForm.get('name').reset();
        this.simulationForm.get('description').reset();
        this.notificationService.showSuccess('Created simulation successfully!');
      },
      error => {
        this.notificationService.showFailure('Failed to create simulation! Please try again.');
      }
    );
  }

  isControlInvalid(formPart: FormGroup, controlName: string): boolean {
    return formPart.get(controlName).invalid;
  }

  getMaterialErrorMessage(factoryConfig, materialIndex: number): string {
    let message = 'This field is required';

    if (factoryConfig.get('materials').controls[materialIndex].hasError('pattern')) {
      message = 'Only letters, numbers, - and _ are allowed.';
    }

    return message;
  }
}
